from django.shortcuts import render
from .models import WeatherData, MarketData, FarmStrategy
from django.http import JsonResponse
import datetime
import numpy as np
from sklearn.linear_model import LinearRegression
from django.shortcuts import render, redirect
from .forms import WeatherDataForm, MarketDataForm, FarmStrategyForm
from .models import WeatherData, MarketData, FarmStrategy
from django.utils.translation import activate

from django.utils.translation import activate

def weather_prediction(request):
    language = request.GET.get('language', 'en')  # Default to English if no language is specified
    activate(language)
    weather_data = WeatherData.objects.order_by('-date')
    context = {
        'weather_data': weather_data
    }
    return render(request, 'farming/weather_prediction.html', context)

def market_analysis(request):
    market_data = MarketData.objects.order_by('-date')  # Order by date descending
    context = {
        'market_data': market_data
    }
    return render(request, 'farming/market_analysis.html', context)

def optimize_strategy(request):
    # Sample AI optimization logic (replace with real optimization logic)
    strategies = FarmStrategy.objects.all()
    # Dummy data for AI model (replace with real data and logic)
    X = np.array([[1], [2], [3], [4], [5]])  # Feature: Day
    y = np.array([1, 3, 2, 5, 4])  # Target: Crop yield

    # Simple linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Predict yield for day 6
    predicted_yield = model.predict([[6]])

    optimized_strategy = {
        "strategy": "Based on AI model, the predicted yield for day 6 is: " + str(predicted_yield[0])
    }
    return render(request, 'farming/optimize_strategy.html', {'optimized_strategy': optimized_strategy})

# def optimize_strategy(request):
#     farm_strategies = FarmStrategy.objects.order_by('-id')  # Order by ID descending (or any other field)
#     context = {
#         'farm_strategies': farm_strategies
#     }
#     return render(request, 'farming/optimize_strategy.html', context)

def add_weather_data(request):
    if request.method == 'POST':
        form = WeatherDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('weather_data_success')
    else:
        form = WeatherDataForm()
    return render(request, 'farming/add_weather_data.html', {'form': form})

def add_market_data(request):
    if request.method == 'POST':
        form = MarketDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('market_data_success')
    else:
        form = MarketDataForm()
    return render(request, 'farming/add_market_data.html', {'form': form})

def add_farm_strategy(request):
    if request.method == 'POST':
        form = FarmStrategyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('farm_strategy_success')
    else:
        form = FarmStrategyForm()
    return render(request, 'farming/add_farm_strategy.html', {'form': form})

def weather_data_success(request):
    return render(request, 'farming/success.html', {'message': 'Weather data added successfully'})

def market_data_success(request):
    return render(request, 'farming/success.html', {'message': 'Market data added successfully'})

def farm_strategy_success(request):
    return render(request, 'farming/success.html', {'message': 'Farm strategy added successfully'})

def landing_page(request):
    return render(request, 'farming/landing_page.html')
