from django.contrib import admin
from .models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_date')
    list_display = ('title', 'status', 'due_date')
    search_fields = ['title']
    fieldsets = (
        (None, {'fields': ('title', 'description')}),
        ('Advanced', {'fields': ('due_date', 'status', 'tags')}),
    )

admin.site.register(Task, TaskAdmin)