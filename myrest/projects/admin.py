from django.contrib import admin

from .models import UserProfile, Project, Task, Developer, Supervisor

admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Developer)
admin.site.register(Supervisor)
