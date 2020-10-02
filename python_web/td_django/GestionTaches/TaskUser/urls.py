from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add', views.add, name="ajout"),
    path('details/<int:cid>', views.details, name="details"),
    path('modifier/<int:id>', views.modifier, name="modifier"),
    path('supprimer/<int:cid>', views.supprimer, name="supprimer"),
]