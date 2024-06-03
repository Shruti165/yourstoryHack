from django.db import models

class WeatherData(models.Model):
    date = models.DateField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    rainfall = models.FloatField()

    def __str__(self):
        return f"Weather on {self.date}"