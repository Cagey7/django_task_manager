from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from .models import *
from .forms import *


navbar = [
    {"title":"Главная страница", "url_name": "index"},
    {"title":"Логин", "url_name": "login"},
    {"title":"Регистрация", "url_name": "register"},
    {"title":"Выполненные задания", "url_name": "completed_tasks"},
    {"title":"Выйти", "url_name": "logout_user"}
]


def index(request):
    if request.user.is_authenticated:
        form = AddTaskForm()
        if request.method == "POST":
            form = AddTaskForm(request.POST)
            if form.is_valid():
                task = form.save(commit=False)
                task.user = request.user
                form.save()
                return redirect("index")
            
        context = {
            "form": form,
            "navbar": navbar,
            "is_completed": False,
            "title": "Главная страница"
        }
        return render(request, "main/index.html", context=context)
    else:
        return redirect("login")


def login(request):
    if request.user.is_authenticated:
        return redirect("index")
    
    if request.method == "POST":
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("index")
    else:
        form = LoginUserForm()
    context = {
        "form": form,
        "navbar": navbar,
        "title": "Логин"
    }
    return render(request, "main/login.html", context=context)


def register(request):
    if request.user.is_authenticated:
        return redirect("index")
    
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterUserForm()
    
    context = {
        "form": form,
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


def task_completed(request):
    task = Task.objects.get(pk=request.POST.get('task_id'))
    task.is_completed = True
    task.save()
    return redirect("index")


def completed_tasks(request):
    context = {
        "navbar": navbar,
        "is_completed": True,
        "title": "Выполненные задания"
    }
    return render(request, "main/completed_tasks.html", context=context)

def logout_user(request):
    logout(request)
    return redirect("index")
