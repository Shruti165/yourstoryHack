from django import forms
from .models import WeatherData, MarketData, FarmStrategy

class WeatherDataForm(forms.ModelForm):
    class Meta:
        model = WeatherData
        fields = ['date', 'temperature', 'humidity', 'precipitation']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'temperature': forms.NumberInput(attrs={'class': 'form-control'}),
            'humidity': forms.NumberInput(attrs={'class': 'form-control'}),
            'precipitation': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class MarketDataForm(forms.ModelForm):
    class Meta:
        model = MarketData
        fields = ['crop_name', 'price', 'date']
        widgets = {
            'crop_name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class FarmStrategyForm(forms.ModelForm):
    class Meta:
        model = FarmStrategy
        fields = ['crop_name', 'planting_date', 'harvest_date', 'strategy_details']
        widgets = {
            'crop_name': forms.TextInput(attrs={'class': 'form-control'}),
            'planting_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'harvest_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'strategy_details': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
