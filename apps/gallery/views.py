from django.shortcuts import render
from .models import Album, Image
from django.db.models import Q
from django.shortcuts import get_list_or_404, get_object_or_404


def gallery(request):
    data = {
        'albums': Album.objects.all().exclude(visibility=False)
    }
    return render(request, 'gallery/gallery.html', data)


def album(request, album_id):
    data = {
        'album': get_object_or_404(Album, ~Q(visibility=False), pk=album_id),
        'images': Image.objects.filter(album__id=album_id, visibility=True)
    }

    return render(request, 'gallery/album.html', data)
