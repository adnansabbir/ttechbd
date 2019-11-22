from django.core.exceptions import ValidationError
from django.db import models


class AffiliationPage(models.Model):
    """Class to contain basic description of the project page"""
    title = models.CharField(default='Affiliations', max_length=20)
    background_image = models.ImageField(upload_to='Site/AffiliationsPage/')

    # Allow only one instance
    def save(self, *args, **kwargs):
        if AffiliationPage.objects.exists() and not self.pk:
            raise ValidationError("Please edit the existing instance, you cannot add more than one")
        return super(AffiliationPage, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class AffiliateProject(models.Model):
    background_image = models.ImageField(upload_to='AffiliateProjects/MainImages/BackgroundImages', null=True,
                                         blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    type = models.ManyToManyField('AffiliateProjectType')
    image = models.ImageField(upload_to='AffiliateProjects/MainImages/')
    visibility = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class AffiliateProjectType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class AffiliateProjectImage(models.Model):
    project = models.ForeignKey(AffiliateProject, models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='AffiliateProjects/ExtraImages/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title
