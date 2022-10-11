import requests
from bs4 import BeautifulSoup

url = "https://kallyas.github.io/cakeshop/"

r = requests.get(url)


soup = BeautifulSoup(r.content, "html.parser")

link_tags = soup.find_all("li")
# print(link_tags)

for index , link in enumerate(link_tags):
    print(index , link.text)