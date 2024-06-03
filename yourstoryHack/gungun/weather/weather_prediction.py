from .models import WeatherData

def predict_weather():
    # Simple example prediction: average of recent data
    recent_data = WeatherData.objects.order_by('-date')[:5]
    if not recent_data:
        return ["No data available for prediction."]

    avg_temp = sum(data.temperature for data in recent_data) / len(recent_data)
    avg_humidity = sum(data.humidity for data in recent_data) / len(recent_data)
    avg_rainfall = sum(data.rainfall for data in recent_data) / len(recent_data)

    return [
        f"Predicted Temperature: {avg_temp:.2f}",
        f"Predicted Humidity: {avg_humidity:.2f}",
        f"Predicted Rainfall: {avg_rainfall:.2f}"
    ]
