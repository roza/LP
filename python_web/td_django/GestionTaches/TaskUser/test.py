import urllib2, httplib
httplib.HTTPConnection.debuglevel = 1           
request = urllib2.Request('http://localhost:8000/taskuser') 
opener = urllib2.build_opener()
f = opener.open(request)