import requests
from bs4 import BeautifulSoup

sait = requests.get("https://7sim.net/ru")
html = BeautifulSoup(sait.content, "lxml")

countries = html.find_all("h4", class_="titlecoutry actv")

database = []

for item in countries:
    country_name = item.find_next("img").get("title")
    all_numbers = item.find_next_sibling("div", class_="row nbox").find_all("div", class_="col-sm-12 col-md-4")

    for temp in all_numbers:
        link = temp.find("a").get("href")
        number = temp.find("a").text

        database.append([country_name, link, number])

print(database)

