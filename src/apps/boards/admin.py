from django.contrib import admin

from apps.boards.models import Board


class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'display_tasks_count')
    search_fields = ('name', )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate_tasks_count()

    def display_tasks_count(self, obj):
        return obj.tasks_count


admin.site.register(Board, BoardAdmin)
