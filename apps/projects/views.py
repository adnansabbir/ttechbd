from django.shortcuts import render
from .models import Project


def project_list(request):
    return render(request, 'projects/project_list.html')
