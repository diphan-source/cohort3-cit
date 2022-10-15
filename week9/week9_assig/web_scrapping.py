"""
1.Find top movies on IMDB since 1980 using web scraping and save the result in a csv file. 
The csv file should have the following columns: title, year, rating, metascore, votes, gross, director, actors, runtime, 
genre, description. The csv file should be sorted by rating in descending order.

"""

from bs4 import BeautifulSoup
import requests
import time 

base_url =f"https://www.imdb.com/search/title/?release_date=1998-01-01,2022-01-01&groups=top_100&count=100"

movie_dict = {}

def scrap_imdb(base_url):
    r = requests.get(base_url)

    soup = BeautifulSoup(r.text, 'html.parser')

    # filter for the movies div 
    movies = soup.find('div', class_='lister-list')
    movies=soup.find_all('div', class_='lister-item-content')

    for index , movie in enumerate(movies):
        title = movie.h3.a.text.strip()
        year = movie.h3.find('span', class_='lister-item-year').text.strip()
        rating = movie.find('div', class_='inline-block ratings-imdb-rating').text.strip()
        metascore = movie.find('div', class_='inline-block ratings-metascore')
        if metascore:
            metascore = metascore.text.strip()
        else:
            metascore = 'No Metascore'
        votes = movie.find('span', attrs={'name':'nv'})['data-value'].strip()
        gross = movie.find('span', attrs={'name':'nv'})['data-value'].strip()
        director = movie.find('p', class_='').text.strip()
        actors = movie.find('p', class_='').text.strip()
        runtime = movie.find('span', class_='runtime').text.strip()
        genre = movie.find('span', class_='genre').text.strip()
        description = movie.find('p', class_='text-muted').text.strip()
        
        movie_dict[index + 1] = {
            "movie_litle":title ,
            "movie_year":year,
            "movie_rating":rating,
            "movie_metascore":metascore,
            "movie_votes":votes,
            "movie_gross":gross,
            "movie_director":director,
            "movie_actor":actors,
            "movie_runtime":runtime,
            "movie_genre":genre,
            "movie_description":description
        }
        
        time.sleep(2)
    
scrap_imdb(base_url)

movie_dict = sorted(movie_dict.items(), key = lambda x: x[1]["movie_rating"], reverse=True)
movie_dict = dict(movie_dict)

with open (f"imdb.csv", "w") as f:
    for key, value in movie_dict.items():
        f.write(f"{key},{value}")
        f.write("\n")
        
print("Done")








