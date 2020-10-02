from django.shortcuts import render, redirect
from django.forms import ModelForm, Textarea
from TaskUser.models import TaskWithUser, User
from django.http import HttpResponse
from django import forms
from django.contrib import messages
from django.urls import reverse

# Create your views here.

# class TaskForm(forms.Form):
#     name = forms.CharField(label = 'Nom de la tâche', max_length=250)
#     description = forms.CharField(label = 'Description de la tâche', widget=forms.Textarea)
#     date_creation = forms.DateField(label = 'Date de création de la tâche')
#     date_rendu = forms.DateField(label = 'Date de rendu de la tâche')
#     user = forms.CharField(label='Utilisateur lié à la tâche')

class TaskForm(ModelForm):
    class Meta:
        model = TaskWithUser
        fields = ('name', 'description', 'date_creation', 'date_rendu', 'user')
        widgets = {
            'description': forms.Textarea(attrs={'cols':20, 'rows': 10,
                'placeholder': 'Entrer votre message ici'}),
            'name': forms.TextInput(), 
            'date_creation' : forms.DateInput(),
            'date_rendu' : forms.DateInput()
        }
        labels = {
            "name": "Nom",
            "description": "Description",
    }

def home(request):
    objects = TaskWithUser.objects.all().order_by('date_rendu')
    return render(request, template_name='list.html',context={'objects':objects})

def add(request):
    form = TaskForm(request.POST)
    if request.method == "POST":
        # on vérifie la validité du formulaire
        if form.is_valid():
            new_tache = form.save()
            #return redirect(reverse('detail', args=[pers_id] ))
            context = {'objects': new_tache}
            return redirect('http://localhost:8000/taskuser/')
    context = {'form' : form}
    return render(request,'add_ModelForm.html', context)

def details(request, cid):
    objects = TaskWithUser.objects.get(pk=cid)
    return render(request, template_name='details.html',context={'objects':objects})

def modifier(request, id):
    # on récupère la personne
    objects = TaskWithUser.objects.get(pk=id)
    # on teste si on est bien en validation de formulaire (POST)
    if request.method == "POST":
        # Si oui on récupère les données postées
        form = TaskForm(request.POST, instance=objects)
        # on vérifie la validité du formulaire
        if form.is_valid():
            form.save()
            messages.success(request, 'Tâche '+objects.name+' modifiée!')
            #return redirect(reverse('detail', args=[pers_id] ))
            context = {'objects': objects}
            return render(request,'details.html',context)
    # Si méthode GET, on présente le formulaire
    form = TaskForm(instance=objects)
    context = {'form': form,'objects': objects}
    return render(request,'modifier.html', context)

def supprimer(request, cid):
    objects = TaskWithUser.objects.get(pk=cid)
    objects.delete()
    messages.success(request, 'Tâche '+objects.name+' supprimée!')
    return redirect('http://localhost:8000/taskuser/')
   