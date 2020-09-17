import requests
from bs4 import BeautifulSoup

mots_a_definir = open("vocabulary.txt", "r")
mots = mots_a_definir.read().split()
fichier = open("definitions.txt", "w")

for m in mots : 
    contenu = requests.get("https://dictionnaire.lerobert.com/definition/" + m)  
    soup = BeautifulSoup(contenu.text, "lxml")  
    definitions = soup.find_all("span", class_="d_dfn", limit=1)
    for defi in definitions: 
        definition = defi.text.encode("latin1").decode()
        fichier.write(m + " : ")
        fichier.write(definition)
        fichier.write("\n\n\n")
fichier.close()
mots_a_definir.close()