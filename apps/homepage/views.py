from django.shortcuts import render
from .models import SliderImages, WhatWeDoSection, WhyChooseUsSection, RecentProjects


def homepage(request):
    data = {
        'sliders': SliderImages.objects.all(),
        'what_we_do_sections': WhatWeDoSection.objects.prefetch_related('cards'),
        'why_choose_us_sections': WhyChooseUsSection.objects.prefetch_related('cards'),
        'recent_projects': RecentProjects.objects.all(),
    }
    return render(request, 'homepage/index.html', data)
