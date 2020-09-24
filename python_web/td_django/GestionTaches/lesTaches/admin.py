from django.contrib import admin
from lesTaches.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display=('name', 'created_date', 'schedule_date', 'colored_due_date')

admin.site.register(Task, TaskAdmin)