from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from apps.boards.models import Board, Col, Comment, Task

admin.site.register(Board)
admin.site.register(Comment)


@admin.register(Col)
class ColModelAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Task)
class TaskAdminModel(admin.ModelAdmin):
    search_fields = ("name",)
    autocomplete_fields = ('col',)
    ordering = ('-updated_at', )
    list_filter = ("status", )
    list_display = ("id", "name", 'view_status', 'created_by')
    list_per_page = 5

    def view_status(self, obj):
        return mark_safe("<i>asfasfsa</i>")

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('created_by')
