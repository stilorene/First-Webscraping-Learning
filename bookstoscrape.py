
#hier scrape ich die Website books to scrape, die es erlaubt zu scrapen
from bs4 import BeautifulSoup
import requests
import re


genre = input("Welches Genre möchtest du? ")
url = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

# with open("website-content.html", "w", encoding="utf-8") as file:
#     file.write(page)

genrelist = doc.find(class_="nav nav-list")
listitems = genrelist.find("li") #Übergeordnetes list
firstlistelement = listitems.find("li") #Untergeordnetes list
listelementtext = firstlistelement.text.strip() #Nur der Text der list 


a_tag = firstlistelement.find("a")
finallink = a_tag['href']
  
print(finallink)



