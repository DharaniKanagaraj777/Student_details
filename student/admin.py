from django.contrib import admin
from student.models import project

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(project, ProjectAdmin)
