from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('album/<int:album_id>', views.album, name='album')
]
