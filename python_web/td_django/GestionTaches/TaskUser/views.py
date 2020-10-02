from django.shortcuts import render, redirect
from django.forms import ModelForm, Textarea
from TaskUser.models import TaskWithUser, User
from django.http import HttpResponse
from django import forms
from django.contrib import messages
from django.urls import reverse

# Create your views here.

class TaskForm(forms.Form):
    name = forms.CharField(label = 'Nom de la tâche', max_length=250)
    description = forms.CharField(label = 'Description de la tâche', widget=forms.Textarea)
    date_creation = forms.DateField(label = 'Date de création de la tâche')
    date_rendu = forms.DateField(label = 'Date de rendu de la tâche')
    user = forms.CharField(label='Utilisateur lié à la tâche')

def home(request):
    objects = TaskWithUser.objects.all().order_by('date_rendu')
    return render(request, template_name='list.html',context={'objects':objects})

def add(request):
    users = User.objects.all()
    return render(request, template_name='add.html', context={'users':users})

def details(request, cid):
    objects = TaskWithUser.objects.get(pk=cid)
    return render(request, template_name='details.html',context={'objects':objects})

def modifier(request, cid):
    objects = TaskWithUser.objects.get(pk=cid)
    users = User.objects.all()
    print(users)
    if request.method == "POST":
        form = TaskForm(request.POST)
        user = User.objects.get(pk=form['user'].data)
        print("user : ")
        print(user)
        matache = TaskWithUser(name = form['name'], description=form['description'], date_creation=form['date_creation'], date_rendu=form['date_rendu'], user=user)
        matache.save()
        messages.success(request, 'Tâche '+objects.name+' modifiée!')
        return render(request, template_name='details.html', context = {'objects': objects})     
    # Si méthode GET, on présente le formulaire
    form = TaskForm(request.POST)
    context = {'form': form,'objects': objects, 'users':users}
    return render(request,'modifier.html', context)

def supprimer(request, cid):
    objects = TaskWithUser.objects.get(pk=cid)
    objects.delete()
    messages.success(request, 'Tâche '+objects.name+' supprimée!')
    return redirect('http://localhost:8000/taskuser/')
   