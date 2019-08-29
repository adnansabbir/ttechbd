from django.shortcuts import render
from .models import ProjectPage, Project


def project_list(request):
    data = {
        'project_page': ProjectPage.objects.first(),
        'projects': Project.objects.all()
    }
    return render(request, 'projects/project_list.html', data)
