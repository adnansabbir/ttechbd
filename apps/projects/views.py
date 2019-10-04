from django.shortcuts import render
from .models import ProjectPage, Project


def project_list(request):
    data = {
        'project_page': ProjectPage.objects.first(),
        'projects': Project.objects.all()
    }
    return render(request, 'projects/project_list.html', data)


def project(request, project_id):
    data = {
        'project_page': ProjectPage.objects.first(),
        'project': Project.objects.get(pk=project_id),
        # 'projects': Project.objects.all()
    }

    # print(ProjectPage.objects.first(), Project.objects.get(pk=project_id))
    return render(request, 'projects/project_single.html', data)
