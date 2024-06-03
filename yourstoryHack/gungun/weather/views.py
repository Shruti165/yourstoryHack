from django.shortcuts import render, redirect
from .models import WeatherData
from .forms import WeatherDataForm
from .weather_prediction import predict_weather
from .ml_model import WeatherPredictor

def home(request):
    if request.method == 'POST':
        form = WeatherDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = WeatherDataForm()

    weather_data = WeatherData.objects.all()
    return render(request, 'weather/home.html', {'form': form, 'weather_data': weather_data})

def predict(request):
    predictions = predict_weather()
    return render(request, 'weather/predict.html', {'predictions': predictions})

def predict_weather(request):
    if request.method == 'POST':
        humidity = float(request.POST['humidity'])
        rainfall = float(request.POST['rainfall'])

        predictor = WeatherPredictor()
        predictor.train()  # Ensure the model is trained
        predicted_temperature = predictor.predict(humidity, rainfall)

        return render(request, 'predictml.html', {'predicted_temperature': predicted_temperature})

    return render(request, 'predictml.html')
