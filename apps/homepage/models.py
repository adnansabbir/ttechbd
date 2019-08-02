from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)
    logo1 = models.ImageField(upload_to='Site/Homepage/Company/', blank=False, null=False)
    logo2 = models.ImageField(upload_to='Site/Homepage/Company/')
    favicon = models.ImageField(upload_to='Site/Homepage/Company/', blank=False, null=True)


class Address(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    phone = models.CharField(max_length=14)
    mobile = models.CharField(max_length=14)
    email = models.CharField(max_length=14)

    ADDRESS_TYPE = (
        ('p', 'Primary'),
        ('s', 'Secondary'),
    )
    address_type = models.CharField(max_length=1, choices=ADDRESS_TYPE)


class SliderImages(models.Model):
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=100)
    bg = models.ImageField(upload_to='Site/Homepage/SliderImages/', blank=False)


class WhatWeDoSection(models.Model):
    title = models.CharField(max_length=50, blank=False)
    sub_title = models.CharField(max_length=100, blank=False)


class WhatWeDoCards(models.Model):
    what_we_do_section = models.ForeignKey(WhatWeDoSection, on_delete=models.CASCADE, related_name='cards')
    icon = models.ImageField(upload_to="Site/Homepage/others", blank=False)
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=100)


class WhyChooseUsSection(models.Model):
    image = models.ImageField(upload_to="Site/Homepage/others")
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)


class WhyChooseUsCards(models.Model):
    why_choose_us_section = models.ForeignKey(WhyChooseUsSection, on_delete=models.CASCADE, related_name='cards')
    icon = models.ImageField(upload_to="Site/Homepage/others", blank=False)
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=100)
