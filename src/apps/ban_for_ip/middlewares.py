from django.core.exceptions import PermissionDenied
from django.utils.deprecation import MiddlewareMixin

from apps.ban_for_ip.utils import get_client_ip, is_banned_ip


class BanForIpMiddleware(MiddlewareMixin):
    def process_request(self, request):
        req_ip = get_client_ip(request)
        if is_banned_ip(req_ip):
            raise PermissionDenied()
