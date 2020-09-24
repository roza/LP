from django.shortcuts import render
from django.forms import ModelForm, Textarea
from myform.models import Contact
from django import forms

# Create your views here.

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name','firstname','email','message')
        widgets = {
            'message':Textarea(attrs={'cols':60,'rows':10}),
        }

class ContactForm2(forms.Form):
    name = forms.CharField(max_length=200,initial="votre nom",label="nom")
    firstname = forms.CharField(max_length=200,initial="votre prenom",label="prenom")
    email = forms.EmailField(max_length=200,label="mel")
    message = forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows':10}))

def contact(request):
    contact_form = ContactForm()
    #returnrender(request,'myform/conctact.html',{'contact_form':contact_form})
    contact_form2 = ContactForm2()
    print('contact view')
    return render(request,'conctact.html',{'contact_form':contact_form,'contact_form2':contact_form2})