from django.contrib import admin
from .models import Task


class MainAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "is_completed")
    list_display_links = ("id",)
    search_fields = ("name", "description")
    list_editable = ("name", "description", "is_completed")
    list_filter = ("name", "description")


admin.site.register(Task, MainAdmin)
