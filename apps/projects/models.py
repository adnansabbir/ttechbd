from django.db import models


class Project(models.Model):
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
    primary_color = models.CharField(max_length=7)
    secondary_color = models.CharField(max_length=7)

    def __str__(self):
        return self.name
