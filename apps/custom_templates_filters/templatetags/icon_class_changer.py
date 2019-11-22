from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter('translate_icon')
@stringfilter
def translate_icon(value: str, replace_with):
    # print(value, replace_with, value.replace('className', replace_with))
    return value.replace('className', replace_with)

# register.filter('translate_icon', translate_icon)
