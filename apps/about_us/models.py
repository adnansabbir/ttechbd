from django.core.exceptions import ValidationError
from django.db import models
from apps.homepage.models import CommonModelClasses
from apps.projects.models import Site


class AboutUsPage(CommonModelClasses):
    """Class to contain basic description of the about us field"""
    title = models.CharField(default='About Us', max_length=20)
    background_image = models.ImageField(upload_to='Site/AboutUs/')

    # Allow only one instance
    def save(self, *args, **kwargs):
        if AboutUsPage.objects.exists() and not self.pk:
            raise ValidationError("Please edit the existing Company, you cannot add more than one company")
        return super(AboutUsPage, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class OurTeamSection(CommonModelClasses):
    """Class containing team member list"""
    title = models.CharField(default='Our Team', max_length=50)
    sub_title = models.CharField(default='We have a Good and Expert Team', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title


class TeamMember(CommonModelClasses):
    """Team member descriptions"""
    section = models.ForeignKey(OurTeamSection, on_delete=models.SET_NULL, null=True, related_name='members')
    name = models.CharField(max_length=80)
    profile_picture = models.ImageField(upload_to='Site/AboutUs/Team/')
    primary_role = models.ForeignKey('TeamMemberRole', on_delete=models.SET_NULL, null=True,
                                     related_name='primary_role')
    other_roles = models.ManyToManyField('TeamMemberRole', related_name='other_roles', blank=True)
    order = models.IntegerField(default=1000)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.name


class TeamMemberRole(models.Model):
    """Roles assigned to team members.
    Can have multiple roles"""
    role_name = models.CharField(max_length=100)

    def __str__(self):
        return self.role_name


class SocialMediaLink(models.Model):
    member = models.ForeignKey(TeamMember, on_delete=models.CASCADE, related_name='links')
    site = models.ForeignKey(Site, on_delete=models.SET_NULL, null=True)
    link = models.CharField(max_length=100)

    def __str__(self):
        return '{} - {}'.format(self.member.name, self.site.name)



