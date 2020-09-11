import requests, re
url='http://www.gutenberg.org/cache/epub/16/pg16.txt'
# si on passe par le proxy univ orleans :
proxy ={"http":"http://wwwcache.univ-orleans.fr:3128/"}
r=requests.get(url ,proxies=proxy)
# si pas de proxy :
# r=requests.get(url)
PeterPan = r.text
print(len(r.text))
r.encoding
it=re.finditer('(The [^.]*)\.',PeterPan)
for i in it:
    print(i.groups ())