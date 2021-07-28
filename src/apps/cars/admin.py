from django.contrib import admin

from apps.cars.models import Car

from apps.cars.models import CarView, CarTag

admin.site.register(Car)
admin.site.register(CarTag)
admin.site.register(CarView)
