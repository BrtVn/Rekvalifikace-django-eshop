from django import template
from django.apps import apps

register = template.Library()


@register.filter
def isinstance_filter(value, arg):
    x = arg.split(".")
    app = x[0]
    model = x[1]
    instance = apps.get_model(app, model)
    return isinstance(value, instance)
