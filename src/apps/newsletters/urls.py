from django.urls import path

from apps.newsletters.views import SubscriberCreateList

app_name = 'newsletters'

urlpatterns = [
    path('subscribers/', SubscriberCreateList.as_view(), name='subscribers'),
]
