from django.shortcuts import render
from .models import AffiliationPage, AffiliateProject


def affiliation_list(request):
    data = {
        'affiliation_page': AffiliationPage.objects.first(),
        'affiliated_projects': AffiliateProject.objects.all().exclude(visibility=False)
    }
    return render(request, 'affiliations/affiliation_list.html', data)


def affiliation(request, project_id):
    data = {
        'affiliation_page': AffiliationPage.objects.first(),
        'project': AffiliateProject.objects.get(pk=project_id),
        'projects': AffiliateProject.objects.all().exclude(visibility=False)
    }

    # print(ProjectPage.objects.first(), Project.objects.get(pk=project_id))
    return render(request, 'affiliations/affiliation_single.html', data)
