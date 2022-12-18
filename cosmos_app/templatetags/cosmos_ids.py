from django import template


register = template.Library()


@register.filter
def last_id(value):
    """Returns the ID of the last element of a list"""
    return value[-1].id