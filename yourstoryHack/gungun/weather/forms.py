from django import forms
from .models import WeatherData

class WeatherDataForm(forms.ModelForm):
    class Meta:
        model = WeatherData
        fields = ['date', 'temperature', 'humidity', 'rainfall']
