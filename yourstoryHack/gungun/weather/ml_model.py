import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from weather.models import WeatherData

class WeatherPredictor:
    def __init__(self):
        self.model = LinearRegression()
        self.scaler = StandardScaler()

    def train(self):
        data = WeatherData.objects.all().values('temperature', 'humidity', 'rainfall')
        dates = WeatherData.objects.all().values('date')
        X = np.array([[record['humidity'], record['rainfall']] for record in data])
        y = np.array([record['temperature'] for record in data])

        X = self.scaler.fit_transform(X)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        self.model.fit(X_train, y_train)

        score = self.model.score(X_test, y_test)
        print(f"Model trained with score: {score}")

    def predict(self, humidity, rainfall):
        X_new = self.scaler.transform([[humidity, rainfall]])
        prediction = self.model.predict(X_new)
        return prediction[0]
