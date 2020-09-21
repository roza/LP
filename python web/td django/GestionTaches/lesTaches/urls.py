from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('home/<name>',views.home,name='home'),
    path('listing', views.task_listing, name='listing'),
]