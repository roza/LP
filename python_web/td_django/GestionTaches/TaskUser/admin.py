from django.contrib import admin
from TaskUser.models import TaskWithUser, User

class TaskUserAdmin(admin.ModelAdmin):
    list_display=('name', 'date_creation', 'colored_due_date', 'description', 'user')

admin.site.register(TaskWithUser, TaskUserAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display=('first_name', 'last_name', 'email')

admin.site.register(User, UserAdmin)