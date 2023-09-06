from django import template
from main.models import *


register = template.Library()


@register.simple_tag()
def get_tasks():
    return Task.objects.all()


@register.inclusion_tag("main/tasks_list.html")
def show_tasks(sort=None):
    if not sort:
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.order_by(sort)
    
    return {"tasks": tasks}