from django.conf import settings
from django.core.cache import cache
from django.utils import timezone


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def is_banned_ip(ip_address) -> bool:
    banned_ips = cache.get(settings.BANNED_IP_REDIS_KEY, [])
    is_banned = next((
        True  # this IP is banned
        for ip_data in banned_ips
        if timezone.now() < ip_data.get('expire_date') and ip_address == ip_data.get('ip')
    ), False)
    return is_banned


def refresh_banned_ips(*args, **kwargs):
    from apps.ban_for_ip.models import BannedIp
    banned_ips = tuple(BannedIp.objects.filter(expire_date__gt=timezone.now()).values('ip', 'expire_date'))
    cache.set(settings.BANNED_IP_REDIS_KEY, banned_ips, 3600*24*100)
