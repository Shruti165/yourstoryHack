from django.db import models
from modeltranslation.translator import TranslationOptions, register

class WeatherData(models.Model):
    date = models.DateField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    precipitation = models.FloatField()

class MarketData(models.Model):
    crop_name = models.CharField(max_length=100)
    price = models.FloatField()
    date = models.DateField()

class FarmStrategy(models.Model):
    crop_name = models.CharField(max_length=100)
    planting_date = models.DateField()
    harvest_date = models.DateField()
    strategy_details = models.TextField()

# class WeatherDataTranslationOptions(TranslationOptions):
#     fields = ('date', 'temperature','humidity','precipitation')
#
# register(WeatherData, WeatherDataTranslationOptions)



