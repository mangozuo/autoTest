from django.contrib import admin
from apiTest.models import Project
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "version", "type", "status", "description",
                    "createTime", "lastUpdateTime", "createUser"]
admin.site.register(Project,ProjectAdmin)


