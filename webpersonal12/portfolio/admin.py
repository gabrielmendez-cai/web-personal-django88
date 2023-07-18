from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
   readonly_fields = ('update', 'created')

admin.site.register(Project, ProjectAdmin)