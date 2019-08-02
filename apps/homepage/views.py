from django.shortcuts import render
from .models import SliderImages, WhatWeDoSection, WhyChooseUsSection


def homepage(request):
    data = {
        'sliders': SliderImages.objects.all(),
        'what_we_do_sections': WhatWeDoSection.objects.prefetch_related('cards'),
        'why_choose_us_sections': WhyChooseUsSection.objects.prefetch_related('cards'),
    }
    return render(request, 'homepage/index.html', data)
