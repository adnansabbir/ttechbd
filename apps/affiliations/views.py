from django.shortcuts import render


def affiliation_list(request):
    data = {
        # 'project_page': ProjectPage.objects.first(),
        # 'projects': Project.objects.all()
    }
    return render(request, 'affiliations/affiliation_list.html', data)


def affiliation(request, project_id):
    data = {
        # 'project_page': ProjectPage.objects.first(),
        # 'project': Project.objects.get(pk=project_id),
        # 'projects': Project.objects.all()
    }

    # print(ProjectPage.objects.first(), Project.objects.get(pk=project_id))
    return render(request, 'affiliations/affiliation_single.html', data)