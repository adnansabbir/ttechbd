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
