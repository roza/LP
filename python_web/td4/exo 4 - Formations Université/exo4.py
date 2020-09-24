import requests
import pandas as pd
from bs4 import BeautifulSoup

fichier = open("formations_univ_orleans.txt", "w")

fichier.write("\n")
fichier.write("*******************************************")
fichier.write("*       Licences Professionnelles         *")
fichier.write("*******************************************")
fichier.write("\n")
for i in range(1, 4, 1) :
    contenu = requests.get("https://formation.univ-orleans.fr/fr/formation/rechercher-une-formation.html?submit-form=&zone-item-id=zoneItem%3A%2F%2Fc8e50408-29b9-4eb9-9b3f-1c209fb2d75b&catalog=odf-2018-2022&title=&textfield=&degree=DP&orgUnit=&place=&page-"+str(i)+"="+str(i))  
    soup = BeautifulSoup(contenu.text, "lxml")  
    licences_pro = soup.find_all("a", class_="know-more")
    for lp in licences_pro : 
        fichier.write("  - " + lp['title'])
        fichier.write("\n")
fichier.write("\n\n\n")
fichier.write("*******************************************")
fichier.write("*           Master en Ecologie            *")
fichier.write("*******************************************")
fichier.write("\n")
contenu = requests.get("https://formation.univ-orleans.fr/fr/formation/rechercher-une-formation.html?submit-form=&zone-item-id=zoneItem%3A%2F%2Fc8e50408-29b9-4eb9-9b3f-1c209fb2d75b&catalog=odf-2018-2022&title=&textfield=ecologie&degree=XB&orgUnit=&place=")  
soup = BeautifulSoup(contenu.text, "lxml")  
masters_eco = soup.find_all("a", class_="know-more")
for me in masters_eco : 
    fichier.write("  - " + me['title'])
    fichier.write("\n")
fichier.write("\n\n\n")
fichier.write("*******************************************")
fichier.write("*          Toute les formations           *")
fichier.write("*******************************************")
fichier.write("\n")
for i in range(1, 18, 1) :
    contenu = requests.get("https://formation.univ-orleans.fr/fr/formation/rechercher-une-formation.html?submit-form=&zone-item-id=zoneItem%3A%2F%2Fc8e50408-29b9-4eb9-9b3f-1c209fb2d75b&catalog=odf-2018-2022&title=&textfield=&degree=&orgUnit=&place=&page-"+str(i)+"="+str(i))  
    soup = BeautifulSoup(contenu.text, "lxml")  
    formations = soup.find_all("a", class_="know-more")
    for f in formations : 
        fichier.write("  - " + f['title'])
        fichier.write("\n")
fichier.close()