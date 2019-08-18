from django.contrib import admin
from . import models

admin.site.register(models.AboutUsPage)
admin.site.register(models.OurTeamSection)
admin.site.register(models.TeamMember)
admin.site.register(models.TeamMemberRole)
admin.site.register(models.SocialMediaLink)

