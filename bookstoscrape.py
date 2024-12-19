
#hier scrape ich die Website books to scrape, die es erlaubt zu scrapen
from bs4 import BeautifulSoup
import requests
import re


input1 = input("Welches Genre möchtest du? ").lower()
url = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

# with open("website-content.html", "w", encoding="utf-8") as file:
#     file.write(page)

genrelist = doc.find(class_="nav nav-list")
listitems = genrelist.find("li") #Übergeordnetes list
listelements = listitems.find_all("li") #Untergeordnete lists, hierbei autom. in eine Listenähnlichen Struktur


# listelementtext = listelements[0].text.strip().lower()
# print(listelementtext)
# if input1 == listelementtext:
#     print("Nice das Format von input1 und listelementtext ist gleich")


for listelement in listelements:
    textfound = listelement.find(string=re.compile(input1, re.IGNORECASE)) #hier bin ich stehen geblieben, leider
    a_tag = listelement.find("a")
    if textfound == True:
        break
    # find_a_tag = textfound.parent
    # foundlink = find_a_tag['href'] #Angezeigt wird nur der relative Link der mit der Basisurl kombiniert werden muss, checkste?

    print(textfound)

# listelementtext = listelements[1].text #Nur der Text der list 
# print(listelementtext)



     
     



  




