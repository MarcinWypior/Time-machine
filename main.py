from bs4 import BeautifulSoup
import requests
import datetime

# destination_time = input("Which year do you want to travel to ? Type the date in this format YYYY-MM-DD: ")
destination_time = "1990-11-16"

try:
    year, month, day = destination_time.split("-")
    destination_datatime = datetime.datetime(year=int(year), month=int(month), day=int(day)).date()

    print(destination_datatime)
except ValueError as e:
    print(e, "enter date in proper format YYYY-MM-DD: ")
except NameError as e:
    print(e, "enter date in proper format YYYY-MM-DD: ")

website = requests.get(url=f"https://www.billboard.com/charts/hot-100/{destination_datatime}")

soup = BeautifulSoup(website.text, 'html.parser')

list_of_divs = soup.find_all(name="div", class_="o-chart-results-list-row-container")

list_of_100_songs =[]
for div in list_of_divs:
    title =div.find(name="h3",id="title-of-a-story").text.strip()
    author_li = div.find_all(name="li",class_="o-chart-results-list__item")
    author = author_li[3].find(name="span").text.strip()
    list_of_100_songs.append((title,author))


# #list_od_divs = soup.find_all(name="div", class_="o-chart-results-list-row-container")
# list_od_divs = soup.select(selector="h3 #title-of-a-story"
#                            )
#
# for div in list_od_divs:
#     print(div.text)

for song in list_of_100_songs:
    print(song)