from django.contrib import admin
from .models import WeatherData, MarketData, FarmStrategy

admin.site.register(WeatherData)
admin.site.register(MarketData)
admin.site.register(FarmStrategy)
