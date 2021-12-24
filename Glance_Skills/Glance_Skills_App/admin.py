from django.contrib import admin

# Register your models here.
from Glance_Skills_App.models import extendeduser,Projects_Comment,ProjectCategory,Project


admin.site.register(extendeduser)
admin.site.register(Project)
admin.site.register(ProjectCategory)
admin.site.register(Projects_Comment)
