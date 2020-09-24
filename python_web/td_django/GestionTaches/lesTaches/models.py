from django.db import models
from datetime import date, timedelta
from django.utils.html import format_html

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True)
    schedule_date = models.DateField(null=True)
    closed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def colored_due_date(self):
        if self.due_date-timedelta(days=7) > date.today():
            color = "green"
        elif self.due_date < date.today() :
            color = "red"
        else : 
            color = "orange"
        return format_html("<span style=color:%s>%s</span>"%(color, self.due_date))
    
    colored_due_date.allow_tags = True
