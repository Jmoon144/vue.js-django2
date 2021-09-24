from todo.models import Todo
from django.contrib import admin

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'todo')
