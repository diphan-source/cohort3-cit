"""
1.Find top movies on IMDB since 1980 using web scraping and save the result in a csv file. 
The csv file should have the following columns: title, year, rating, metascore, votes, gross, director, actors, runtime, 
genre, description. The csv file should be sorted by rating in descending order.
The csv file should have the following columns: title, year, rating, metascore, votes, gross, director, actors, runtime,
genre, description. The csv file should be sorted by rating in descending order.

2.Scrap Hacker News project and save the result in a csv file. 
The csv file should have the following columns: title, link, points, comments, author, rank. 
The csv file should be sorted by rank in ascending order.

"""

# solutions 


from bs4 import BeautifulSoup
import requests


# https://www.imdb.com/find?q=top+movies+since+1980&ref_=nv_sr_sm
search_movies = input("What movies do you want to search for?: ")
base_url =f"https://www.imdb.com/find?q={search_movies.replace(' ', '+')}"

r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html.parser')

print(soup.prettify())


