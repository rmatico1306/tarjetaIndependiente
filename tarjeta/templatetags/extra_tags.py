from django import template
from django.template.defaultfilters import truncatechars


register = template.Library()    

@register.simple_tag
def add_args(*args, **kwargs):
    chars = kwargs.get('chars')
    return truncatechars(' '.join([str(arg) for arg in args]), chars)