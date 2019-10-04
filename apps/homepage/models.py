from django.core.exceptions import ValidationError
from django.db import models
from apps.projects.models import Project


class CommonModelClasses(models.Model):
    """A model class that will be inherited by model classes to share common fields"""
    visibility = models.BooleanField(default=True)


class Company(models.Model):
    company_name = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True, null=True)
    logo_light = models.ImageField(upload_to='Site/Homepage/Company/', blank=False, null=False)
    logo_dark = models.ImageField(upload_to='Site/Homepage/Company/')
    favicon = models.ImageField(upload_to='Site/Homepage/Company/', blank=False, null=True)

    color1 = models.CharField(max_length=7, default='#ff5e15')

    # Allow only one instance
    def save(self, *args, **kwargs):
        if Company.objects.exists() and not self.pk:
            raise ValidationError("Please edit the existing Company, you cannot add more than one company")
        return super(Company, self).save(*args, **kwargs)


class Address(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    phone = models.CharField(max_length=14, null=True, blank=True)
    mobile = models.CharField(max_length=14)
    email = models.EmailField(max_length=255)

    ADDRESS_TYPE = (
        ('p', 'Primary'),
        ('s', 'Secondary'),
    )
    address_type = models.CharField(max_length=1, choices=ADDRESS_TYPE, default='s')

    # If set as primary address and a primary address already exist make it secondary
    def save(self, *args, **kwargs):
        try:
            if Address.objects.exists() and not self.pk:
                address = Address.objects.get(address_type='p')
                address.address_type = 's'
                address.save()
        except Address.DoesNotExist:
            pass
        super(Address, self).save(*args, **kwargs)


class SliderImages(models.Model):
    title = models.CharField(max_length=100)
    show_title = models.BooleanField(default=True)
    sub_title = models.CharField(max_length=200, null=True, blank=True)
    bg = models.ImageField(upload_to='Site/Homepage/SliderImages/', blank=False)

    def __str__(self):
        return self.title or ''


class WhatWeDoSection(models.Model):
    title = models.CharField(max_length=50, blank=False)
    sub_title = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.title


class WhatWeDoCards(models.Model):
    what_we_do_section = models.ForeignKey(WhatWeDoSection, on_delete=models.CASCADE, related_name='cards')
    icon = models.ForeignKey('FlatIconsClassName', on_delete=models.SET_NULL, null=True, blank=False)
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class WhyChooseUsSection(models.Model):
    image = models.ImageField(upload_to="Site/Homepage/others")
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class WhyChooseUsCards(models.Model):
    why_choose_us_section = models.ForeignKey(WhyChooseUsSection, on_delete=models.CASCADE, related_name='cards')
    icon = models.ForeignKey('FlatIconsClassName', on_delete=models.SET_NULL, null=True, blank=False)
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class RecentProjects(models.Model):
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=100)
    projects = models.ManyToManyField(Project)

    def __str__(self):
        return self.title


class Footer(models.Model):
    menu_1_title = models.CharField(max_length=25)
    menu_1_links = models.ManyToManyField('FooterLink', related_name='menu_1_links')

    menu_2_title = models.CharField(max_length=25)
    menu_2_links = models.ManyToManyField('FooterLink', related_name='menu_2_links')

    menu_3_title = models.CharField(max_length=25)
    menu_3_links = models.ManyToManyField('FooterLink', related_name='menu_3_links')

    # Allow only one instance
    def save(self, *args, **kwargs):
        if Footer.objects.exists() and not self.pk:
            raise ValidationError("Please edit the existing Footer, you cannot add more than one footer")
        return super(Footer, self).save(*args, **kwargs)


class FooterLink(models.Model):
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class FlatIconsClassName(models.Model):
    class_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
