# from bs4 import BeautifulSoup
# import re


# with open("index.html", "r") as f:
#     doc = BeautifulSoup(f, "html.parser")

# # tag = doc.find(["p", "div", "li"])
# # tags = doc.find_all(["option"], text="Undergraduate", value="udnergraduate")
# # tag['value'] = 'new value'
# # tag['colour'] = 'blue'
# # print(tag.attrs)

# # tags = doc.find_all(string=re.compile("\$.*"), limit = 5)
# tags = doc.find_all("input", type="text")
# for tag in tags:
#     # print(tag.strip())
#     tag['placeholder'] = "I changed your, muhaha!"

# with open("changed.html", "w") as file: 
#     file.write(str(doc))




