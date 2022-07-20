#from django.template import loader
from django import template


register = template.Library()

@register.filter(name="get_item", is_safe=True)
def get_item(dictionary, key):
     return dictionary.get(str(key))


     