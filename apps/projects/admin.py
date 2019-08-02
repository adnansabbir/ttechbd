from django.contrib import admin
from . import models

admin.site.register(models.Project)
admin.site.register(models.ProjectImage)
admin.site.register(models.Link)
admin.site.register(models.Site)
admin.site.register(models.ProjectType)
