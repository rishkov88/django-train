from django import template

register = template.Library()

@register.filter(name="addcent")
def addcent(value):
    return value + 200

@register.filter(name="couper")
def couper(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, "yy")

@register.filter(name="minuscule")
def minuscule(value):  # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()