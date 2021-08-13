from django.contrib import admin
# Register your models here.
from django.utils.safestring import mark_safe

from apps.users.models import TrelloUser


@admin.register(TrelloUser)
class TrelloUserAdminModel(admin.ModelAdmin):
    list_display = ("id", "view_full_name", 'view_avatar')

    def view_avatar(self, obj):
        if obj.avatar:
            return mark_safe(f'<img width="90" src="{obj.avatar.url}">')
        return "No selected"
    view_avatar.short_description = 'Avatar'

    def view_full_name(self, obj: TrelloUser):
        return obj.get_full_name()
