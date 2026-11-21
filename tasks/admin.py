from django.contrib import admin
from .models import Tasks
# Register your models here.

@admin.register(Tasks)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title","done","created")