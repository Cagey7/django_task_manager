from django.http import HttpResponse
from django.shortcuts import render
from .models import Task


navbar = [
    {"title":"Главная страница", "url_name": "index"},
    {"title":"Логин", "url_name": "login"},
    {"title":"Регистрация", "url_name": "register"}
]


def index(request):
    context = {
        "navbar": navbar,
        "title": "Главная страница"
    }
    return render(request, "main/index.html", context=context)


def login(request):
    context = {
        "navbar": navbar,
        "title": "Логин"
    }
    return render(request, "main/login.html", context=context)


def register(request):
    context = {
        "navbar": navbar,
        "title": "Регистрация"
    }
    return render(request, "main/register.html", context=context)


def task(request, task_id):
    task = Task.objects.get(pk=task_id)
    context = {
        "task": task,
        "navbar": navbar,
        "title": "Задание",
    }
    return render(request, "main/task.html", context=context)