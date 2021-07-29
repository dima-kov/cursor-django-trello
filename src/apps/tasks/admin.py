from django.contrib import admin

from apps.tasks.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'assigned_to')
    autocomplete_fields = ('board', )


admin.site.register(Task, TaskAdmin)
