from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='auto_br')
@stringfilter
def auto_br(value, limits):
    
    try:
        limits = int(limits)
    except ValueError as e:
        limits = 10

    split_value = value.split('<br>')
        
    split_again = []
    for pease in split_value:
        split_again.extend([pease[i: i+limits] for i in range(0, len(pease), limits)])

    value = '<br>'.join(split_again)
    return mark_safe(value)
