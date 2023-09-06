from django.contrib import admin
from .models import Task


class MainAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    list_display_links = ("id",)
    search_fields = ("name", "description")
    list_editable = ("name", "description")
    list_filter = ("name", "description")


admin.site.register(Task, MainAdmin)
