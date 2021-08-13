from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

from apps.api_v1.views import HealthcheckView

app_name = 'api_v1'

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='auth_token'),
    path('healthcheck/', HealthcheckView.as_view(), name='healthcheck'),
    path('boards/', include('apps.boards.urls')),
]
