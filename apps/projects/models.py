from django.db import models
from django.core.exceptions import ValidationError

# from apps.homepage.models import CommonModelClasses


class ProjectPage(models.Model):
    """Class to contain basic description of the project page"""
    title = models.CharField(default='Our Projects', max_length=20)
    background_image = models.ImageField(upload_to='Site/ProjectPage/')

    # Allow only one instance
    def save(self, *args, **kwargs):
        if ProjectPage.objects.exists() and not self.pk:
            raise ValidationError("Please edit the existing instance, you cannot add more than one")
        return super(ProjectPage, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Project(models.Model):
    background_image = models.ImageField(upload_to='Projects/MainImages/BackgroundImages', null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    type = models.ManyToManyField('ProjectType')
    image = models.ImageField(upload_to='Projects/MainImages/')

    def __str__(self):
        return self.title


class ProjectType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='Projects/ExtraImages/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    visibility = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Link(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='links')
    media = models.ForeignKey('Site', on_delete=models.SET_NULL, null=True)
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.project


class Site(models.Model):
    icon = models.ImageField(upload_to='Projects/Sites/icons', null=True, blank=True)
    name = models.CharField(max_length=50)
    icon_class_name = models.CharField(max_length=50, null=True, blank=True)
    primary_color = models.CharField(max_length=7, null=True, blank=True)
    secondary_color = models.CharField(max_length=7, null=True, blank=True)

    def __str__(self):
        return self.name
