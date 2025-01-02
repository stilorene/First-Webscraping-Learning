
#hier scrape ich die Website books to scrape, die es erlaubt zu scrapen
from bs4 import BeautifulSoup
import requests
import re
import webbrowser



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
                genreurl = a_tag['href'] #Angezeigt wird nur der relative Link der mit der Basisurl kombiniert werden muss, checkste?
                combinedlink = url + genreurl #Der kombinierte Link, auf einfache Art gelöst
                # webbrowser.open("page-1.html") #Öffnet den Link im Browser
                 
                break

            print(f"Gefundener Text: {textfound.strip()}")
    return combinedlink #Wie ein Prozess, das ist das Output der Funktion

                

pagesurls = []
def findnextpage(combinedlink):

    while True:
        page = requests.get(combinedlink).text
        pages = BeautifulSoup(page, "html.parser")
        findbutton = pages.find("li", class_= "next")

        if findbutton is None: 
            print("Keine Weiteren Seiten gefunden!")
            break
        
        else: 
            buttonlink = findbutton.find("a", href=True)
            pagenumber = buttonlink["href"]


            base_url, last_element = combinedlink.rsplit("/", 1)

            # Das letzte Element ersetzen
            new_last_element = pagenumber
            new_url = f"{base_url}/{new_last_element}"

        print(f"Der Link zur nächsten Seite: /{new_url} ")
        combinedlink = new_url
        pagesurls.append(new_url)
    

    



def foundbooks(combinedlink, pagesurls):

    genrepage = requests.get(combinedlink).text
    genredoc = BeautifulSoup(genrepage, "html.parser")
    bookinfo = genredoc.find("ol", class_="row") #suche nach den einzelnen Buchelementen
    booklist = bookinfo.find_all("li") #findet liste und deren Bookpods
    bookdict = {index: element.find("h3").text for index, element in enumerate(booklist, start=1) } #erstellt ein dict und gibt ihnen den Key: index

    for index, element in bookdict.items():
        print(index, element)

    # bookdirect = int(input("\nWelches Buch interessiert sie genauer?\nZahl eintippen: "))

    # print(bookdict[bookdirect])


    for pageurl in pagesurls:
        genrepage = requests.get(pageurl).text
        genredoc = BeautifulSoup(genrepage, "html.parser")
        bookinfo = genredoc.find("ol", class_="row") #suche nach den einzelnen Buchelementen
        booklist = bookinfo.find_all("li") #findet liste und deren Bookpods
        bookdict = {index: element.find("h3").text for index, element in enumerate(booklist, start=1) } #erstellt ein dict und gibt ihnen den Key: index

        for index, element in bookdict.items():
            print(index, element)

    






# Funktionen um Seiteninhalt und deren Bücher zu scrapen Anfang
combinedlink = getlinkgenre(listelements, url, input1)
findnextpage(combinedlink)
foundbooks(combinedlink, pagesurls)

     




  




