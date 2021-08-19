from django.contrib import admin

# Register your models here.
from apps.ban_for_ip.models import BannedIp

admin.site.register(BannedIp)
