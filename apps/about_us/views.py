from django.shortcuts import render
from .models import AboutUsPage, OurTeamSection


def about_us(request):
    data = {
        'about_us': AboutUsPage.objects.filter(visibility=True).first(),
        'our_team_sections': OurTeamSection.objects.filter(visibility=True)
    }
    return render(request, 'about_us/about_us.html', data)
