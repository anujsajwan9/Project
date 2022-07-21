from django.contrib import admin


# Register your models here.
from Glance_Skills_App.models import extendeduser,Projects_Comment,ProjectCategory,Project 
from Glance_Skills_App.models.projects import Project_CommentsReply

admin.site.register(extendeduser)
admin.site.register(Project)
admin.site.register(ProjectCategory)
admin.site.register(Projects_Comment)
admin.site.register(Project_CommentsReply)
