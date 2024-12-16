from bs4 import BeautifulSoup
import requests
import re


#Funktionen für das Captcha
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
max_requests = 10
request_count = 0

for page in range(1, 21):  # Beispiel für 20 Seiten
    if request_count >= max_requests:
        print("Wartezeit, um Blockierung zu vermeiden...")
        time.sleep(60)  # Warte 1 Minute
        request_count = 0

    url = f"https://www.newegg.com/p/pl?d=4070&page={page}"
    response = requests.get(url, headers=headers)
    if "CAPTCHA" in response.text:
        print("CAPTCHA-Seite erkannt, warte länger...")
        time.sleep(600)  # 5 Minuten warten
        continue  # Zur nächsten Seite springen

    print(f"Seite {page} erfolgreich abgerufen")
    request_count += 1
    time.sleep(10)  # Warte 10 Sekunden





gpu = input("Welches Produkt suchst du? ")

url = f"https://www.newegg.com/p/pl?d={gpu}"

page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")
with open("webpage.html", "w", encoding="utf-8") as file:
    file.write(page)



page_text = doc.find(class_ ="list-tool-pagination-text").strong
print(page_text)

pages = int(str(page_text).split('/')[-2].split(">")[-1][:-1])


for page in range(1, pages + 1):
    url = f"https://www.newegg.com/p/pl?d={gpu}&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    div = doc.find(class_ = "item-cells-wrap border-cells short-video-box items-list-view is-list")
    items = div.find_all(text=re.compile(gpu))


    for item in items: 
        print(item)

