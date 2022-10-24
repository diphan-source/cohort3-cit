
import requests 
from bs4 import BeautifulSoup
import lxml
from flask import Flask, Blueprint, render_template , redirect ,request
import json
from cbs_news.models import CBSNews


cbs_views = Blueprint('cbs_views', __name__)


def get_cbs_news():
    base_url = 'https://www.cbsnews.com/latest/rss/main'
    response = requests.get(base_url)

    soup = BeautifulSoup(response.text, features= 'xml')
    # print(soup.prettify())

    rows = soup.find_all('item')

    news_data = []

    for row in rows:
        title = row.find('title').text
        Link = row.link.next_sibling.text.strip()
        image = row.find('image').text
        description = row.find('description').text
        news_data.append({
            'title': title,
            'link': Link,
            'image': image,
            'description': description
        })
        # print(news_data)
    return news_data


@cbs_views.route('/cbs_news', methods=['GET' , 'POST'])
def get_news_data():
    if request.method == 'GET':
        # news from cbs_news site 
        data = get_cbs_news()
        
        # check data in the database 
        views = CBSNews.get_all_news()
        
        for news in data:
            # check if the news is in the database 
            if news not in views:
                # add the news to the database 
                cbs_news = CBSNews(title=news['title'], link=news['link'], image=news['image'], description=news['description'])
                cbs_news.save()
            else:
                continue 
            
        return {'data': [news.serialize() for news in CBSNews.get_all_news()]}
        
    