from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("logout_user", views.logout_user, name="logout_user"),
    path("task/<int:task_id>", views.task, name="task")
]
