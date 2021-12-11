from django import template

register = template.Library()

@register.simple_tag()
def find_in(str,word):
    return str.find(word)

@register.simple_tag()
def equating(str):
    return str
