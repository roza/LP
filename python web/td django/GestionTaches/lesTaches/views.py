from django.shortcuts import render
from django.http import HttpResponse
from lesTaches.models import Task

#def task_listing(request):
#    from django.template import Template,Context 
#    objets=Task.objects.all().order_by('due_date') 
#    return render(request,template_name='list.html', context={'objets':objets})

def task_listing(request):
    objects = Task.objects.all().order_by('due_date')
    return render(request, template_name='list2.html',context={'objects':objects})

#def task_listing2(request): 
#    objets=Task.objects.all().order_by('due_date')
#    return render(request,'lesTaches/other.html',{'taches': objets})

def home(request, name=None) : 
    if name is None : 
        return HttpResponse("Salut à toi inconnu")
    else :
        return HttpResponse('bonjour ' + name)
