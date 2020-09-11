import requests
from bs4 import BeautifulSoup
UNI = requests.get("http://www.univ-orleans.fr")
#print(UNI.text)
soup = BeautifulSoup(UNI.text, "lxml")
print(soup.h1.text)
#print(soup.div.text)
liens = soup.find_all('a', href=True) #tout les liens de la page
divs = soup.find_all('div')) #tout les divs de la page
divs = soup.find_all('div'), class_="header-composante") #toute les divs de la classe header-composante