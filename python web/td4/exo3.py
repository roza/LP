import requests
import pandas as pd
from bs4 import BeautifulSoup
contenu = requests.get("https://stackoverflow.com/search?q=beautifulsoup")  
soup = BeautifulSoup(contenu.text, "lxml")  
questions = soup.find_all("div", class_="question-summary", limit=10)
res = {}
res['question'] = list()
res['vote'] = list()
res['rep'] = list()
for q in questions :
    question = q.find_all("h3")
    vote = q.find("span", class_="vote-count-post")
    reponses = q.find("div", class_=(["status answered", "status answered-accepted"]))
    r = reponses.find("strong")
    for quest in question : 
        res['question'].append(quest.text)
        res['vote'].append(int(vote.text))
        res['rep'].append(int(r.text))
        #res.append((quest.text, int(vote.text), int(r.text)))
print(res)
df = pd.DataFrame(res, columns= ['Questions', 'Votes', 'Réponses'])

df.to_csv (r'/home/fbazire/Bureau/LP/python web/td4', index = False, header=True)

print (df)