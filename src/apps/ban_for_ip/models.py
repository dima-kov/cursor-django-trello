from datetime import timedelta

from django.db import models

# Create your models here.
from django.db.models.signals import post_delete, post_save
from django.utils import timezone

from apps.ban_for_ip.utils import refresh_banned_ips
from common.models import BaseDateAuditModel


def _default_ban_ttl():
    return timezone.now() + timedelta(days=365 * 100)


class BannedIp(BaseDateAuditModel):
    ip = models.GenericIPAddressField()
    expire_date = models.DateTimeField(default=_default_ban_ttl)

    def __str__(self):
        return f'{self.ip} TTL: {self.expire_date}'


post_save.connect(refresh_banned_ips, sender=BannedIp)
post_delete.connect(refresh_banned_ips, sender=BannedIp)
