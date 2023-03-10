from bs4 import BeautifulSoup
from csv import *
import requests
#pip install requests 
#pip install beautifulsoup4
#pip install lxml
page=requests.get("https://www.yallakora.com/Match-Center")
src=page.content ### html code and css and java
cham=[]
teama=[]
#parsing
soup=BeautifulSoup(src,"lxml")
Match_delails=[]
championship=soup.find_all("div",{"class":"matchCard"})
print(championship)

for i in range(len(championship)):
    cham.append(championship[i].find("div",{"class":"teams teamA"}).text.split())
print(cham)
print(len(cham))
# for i in range(len(cham)):
#     teama.append(cham[i].find("li").find("div",{"class":"teams teamA"}).text)
# print(teama)

# for i in range(len(championship)):
#     cham.append(championship[i])
# print(cham)
#print(title_championship)

# print(championship)

# for x in range(len(championship)):
#     teama.append(championship[x].find("section",{"class":"mtchCntrContainer maxWidth"}).find("div",{"class":"2781 matchCard matchesList"}).find('ul').find("div",{"class":"teams teamA"}).text)

# print(teama)
for id in range(len(cham)):
    with open("ali.txt","a") as w:
        w.write("\n"+"".join (str(cham[id])))