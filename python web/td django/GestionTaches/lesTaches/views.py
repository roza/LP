from django.shortcuts import render
from django.http import HttpResponse

def home(request, name=None) : 
    if name is None : 
        return HttpResponse("Salut à toi inconnu")
    else :
        return HttpResponse('bonjour ' + name)
