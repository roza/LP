from django.db import models
from datetime import date, timedelta
from django.utils.html import format_html

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__ (self):
        return self.first_name + " " + self.last_name

class TaskWithUser(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    date_creation  = models.DateField(auto_now_add=True)
    date_rendu = models.DateField(null=True)
    closed = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name = "user", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def colored_due_date(self):
        if self.date_rendu-timedelta(days=7) > date.today():
            color = "green"
        elif self.date_rendu < date.today() :
            color = "red"
        else : 
            color = "orange"
        return format_html("<span style=color:%s>%s</span>"%(color, self.date_rendu))
    
    colored_due_date.allow_tags = True