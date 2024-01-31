from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings


class Task(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название")
    description = models.CharField(max_length=1024, verbose_name="Описание")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True)
    is_completed = models.BooleanField(default=False)

    

    def __str__(self):
        return f"Название: {self.name}, описание: {self.description}, пользователь: {self.user.username}"
    

    def get_absolute_url(self):
        return reverse("task", kwargs={"task_id":self.pk})
    

    class Meta:
        verbose_name = "Задания"
        verbose_name_plural = "Задания"
        ordering = ["name", "description"]