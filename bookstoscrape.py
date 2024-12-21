
#hier scrape ich die Website books to scrape, die es erlaubt zu scrapen
from bs4 import BeautifulSoup
import requests
import re



input1 = input("Welches Genre möchtest du? ").lower()
url = "https://books.toscrape.com/"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")


genrelist = doc.find(class_="nav nav-list")
listitems = genrelist.find("li") #Übergeordnetes list
listelements = listitems.find_all("li") #Untergeordnete lists, hierbei autom. in eine Listenähnlichen Struktur

def getlinkgenre(listelements, url, input1):
    for listelement in listelements:
        textfound = listelement.find(string=re.compile(input1, re.IGNORECASE)) #re.IGNORECASE ignoriert Groß- und Kleinschreibung
        
        if textfound: #obs halt True ist, ja dann mach das
            a_tag = listelement.find("a")
            if a_tag:
                foundlink = a_tag['href'] #Angezeigt wird nur der relative Link der mit der Basisurl kombiniert werden muss, checkste?
                combinedlink = url + foundlink
                # webbrowser.open(foundlink) #Öffnet den Link im Browser
                 
                break

            print(f"Gefundener Text: {textfound.strip()}")
    return combinedlink 
                

# Funktionen um Seiteninhalt und deren Bücher zu scrapen Anfang
combinedlink = getlinkgenre(listelements, url, input1)
if combinedlink:
    print(f"Gefundener kombinierter Link: {combinedlink}")
else:
    print("Kein Link gefunden")


genrepage = requests.get(combinedlink).text
genredoc = BeautifulSoup(genrepage, "html.parser")

bookinfo = genredoc.find("ol", class_="row") #suche nach den einzelnen Buchelementen
booklist = bookinfo.find_all("li")

for element in booklist:
    booktitle = element.find("h3").text
    #Suche nach title
    print(booktitle)

# booktitle = bookinfo.find("li") #.find("h3").text




     
     



  




