from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=100)
    thumbnail_url = models.URLField(max_length=250)
    cover_image_url = models.URLField(max_length=250)
    visibility = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    thumbnail_url = models.URLField(max_length=250)
    image_url = models.URLField(max_length=250)
    album = models.ManyToManyField('Album')
    visibility = models.BooleanField(default=True)

    def __str__(self):
        return self.title or 'No Title'
