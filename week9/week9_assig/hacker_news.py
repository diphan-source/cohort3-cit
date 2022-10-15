
"""
2.Scrap Hacker News project and save the result in a csv file. 
The csv file should have the following columns: title, link, points, comments, author, rank. 
The csv file should be sorted by rank in ascending order.

"""

from bs4 import BeautifulSoup
import requests 
import time 


# ask user to enter the number of pages to scrap
page_end = input("Enter the number of pages you want to scrap: ")

# pages to scrap
for page in range(1, int(page_end) + 1):
    base_url =f"https://news.ycombinator.com/news?p={page}"
    
    
    hacker_news_dict = {}

    # function to scrap hacker news
    def scrap_hacker_news(base_url):
        r = requests.get(base_url)
        soup = BeautifulSoup(r.text, 'html.parser')
        # filter for getting the body of the page 
        news = soup.find('tbody')
        news=soup.find_all('tr', class_='athing')
        news_details = soup.find_all('span', class_='subline')
        # print(soup.prettify())
        # print(news)
        # loop through to get each detail of the news
        for index , news in enumerate(news):
            title = news.find('span', class_='titleline').find('a').text.strip()
            link = news.find('span', class_='titleline').find('a')['href'].strip()
            rank = news.find('span', class_='rank').text.strip()
            for news_detail in news_details:
                points = news_detail.find('span', class_='score').text.strip()
                comments = news_detail.find_all('a')[-1]
                if comments:
                    comments = comments.text.strip()
                else:
                    comments = 'No comments'
                author =news_detail.find_all('a')[0].text.strip()
                
                # return the result in a dictionary
                hacker_news_dict[index + 1] = {
                    "news_title":title ,
                    "news_link":link,
                    "news_points":points ,
                    "news_comments":comments,
                    "news_author":author,
                    "news_rank":rank,
                }
            
            time.sleep(1)
            
scrap_hacker_news(base_url)

# sort the result by rank in ascending order
hacker_news_dict = sorted(hacker_news_dict.items(), key=lambda x: x[-1]['news_rank'])
hacker_news_dict = dict(hacker_news_dict)

# store the result in a csv file
with open ('hacker_news.csv', 'w') as f:
    for key, value in hacker_news_dict.items():
        f.write(f"{key},{value}")
        f.write('\n')
        
print("Done")

