from bs4 import BeautifulSoup
import csv
import requests 
from itertools import zip_longest

name = []
capital = []
population = []
area_km2 = []

result = requests.get("https://www.scrapethissite.com/pages/simple/")
src = result.content
soup = BeautifulSoup(src ,"lxml")

names = soup.find_all("h3", class_ = "country-name")
capitals = soup.find_all("span", class_ = "country-capital")
populations = soup.find_all("span", class_ = "country-population")
area_km2s = soup.find_all("span", class_ = "country-area")

for i in range(len(names)):
    name.append(names[i].text.strip())
    capital.append(capitals[i].text.strip())
    population.append(populations[i].text.strip())
    area_km2.append(area_km2s[i].text.strip())

file_list = [name, capital, population, area_km2]
exported = zip_longest(*file_list)
with open("C:/Users/adnan/OneDrive/Desktop/csv/work.csv", "w", encoding='UTF-8') as my_file:
    wr = csv.writer(my_file)
    wr.writerow(["Country Name", "Capital", "Population", "Area (km2)"])
    wr.writerows(exported) 

