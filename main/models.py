from django.db import models
from django.urls import reverse


class Task(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название")
    description = models.CharField(max_length=1024, verbose_name="Описание")
    

    def __str__(self):
        return f"Название: {self.name}, описание: {self.description}"
    

    def get_absolute_url(self):
        return reverse("task", kwargs={"task_id":self.pk})
    

    class Meta:
        verbose_name = "Задания"
        verbose_name_plural = "Задания"
        ordering = ["name", "description"]