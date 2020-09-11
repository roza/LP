import requests
from bs4 import BeautifulSoup
contenu = requests.get("https://stackoverflow.com/search?q=beautifulsoup")  
soup = BeautifulSoup(contenu.text, "lxml")  
questions = soup.find_all("div", class_="question-summary", limit=10)
for q in questions :
    question = q.find_all("h3")
    vote = q.find("span", class_="vote-count-post")
    reponses = q.find("div", class_=(["status answered", "status answered-accepted"]))
    r = reponses.find("strong")
    rep = list()
    for quest in question : 
        res = list()
        res.append(quest.text)
        res.append(vote.text)
        res.append(r.text)
        rep.append(res)
print(rep)
        