from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("logout_user", views.logout_user, name="logout_user"),
    path("task/<int:task_id>", views.task, name="task"),
    path("task_completed", views.task_completed, name="task_completed"),
    path("completed_tasks", views.completed_tasks, name="completed_tasks")
]
