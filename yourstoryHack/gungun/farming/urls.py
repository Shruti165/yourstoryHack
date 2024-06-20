from django.urls import path
from . import views

urlpatterns = [
    path('gungun/', views.landing_page, name='landing_page'),
    path('add_weather/', views.add_weather_data, name='add_weather_data'),
    path('add_market/', views.add_market_data, name='add_market_data'),
    path('add_strategy/', views.add_farm_strategy, name='add_farm_strategy'),
    path('weather/', views.weather_prediction, name='weather_prediction'),
    path('market/', views.market_analysis, name='market_analysis'),
    path('optimize/', views.optimize_strategy, name='optimize_strategy'),
    path('weather_success/', views.weather_data_success, name='weather_data_success'),
    path('market_success/', views.market_data_success, name='market_data_success'),
    path('strategy_success/', views.farm_strategy_success, name='farm_strategy_success'),
]

