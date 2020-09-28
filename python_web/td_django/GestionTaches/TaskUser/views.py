from django.shortcuts import render
from TaskUser.models import TaskWithUser
from django.http import HttpResponse
# Create your views here.

def home(request):
    objects = TaskWithUser.objects.all().order_by('date_rendu')
    return render(request, template_name='list.html',context={'objects':objects})

def add(request):
    return render(request, template_name='add.html')

def details(request, cid):
    objects = TaskWithUser.objects.get(pk=cid)
    return render(request, template_name='details.html',context={'objects':objects})

def modifier(request, cid):
    objects = TaskWithUser.objects.get(pk=cid)
    return render(request, template_name='modifier.html',context={'objects':objects})

def supprimer(request, cid):
    objects = TaskWithUser.objects.get(pk=cid)
    return render(request, template_name='supprimer.html',context={'objects':objects})