# farming/management/commands/populate_data.py

import json
from django.core.management.base import BaseCommand
from farming.models import WeatherData, MarketData, FarmStrategy

class Command(BaseCommand):
    help = 'Populate database with data from JSON file'

    def handle(self, *args, **options):
        with open('farming/data.json', 'r') as f:
            data = json.load(f)

            # Populate WeatherData model
            weather_data = data['weather_data']
            for item in weather_data:
                WeatherData.objects.create(
                    date=item['date'],
                    temperature=item['temperature'],
                    humidity=item['humidity'],
                    precipitation=item['precipitation']
                )

            # Populate MarketData model
            market_data = data['market_data']
            for item in market_data:
                MarketData.objects.create(
                    crop_name=item['crop_name'],
                    price=item['price'],
                    date=item['date']
                )

            # Populate FarmStrategy model
            farm_strategies = data['farm_strategies']
            for item in farm_strategies:
                FarmStrategy.objects.create(
                    crop_name=item['crop_name'],
                    planting_date=item['planting_date'],
                    harvest_date=item['harvest_date'],
                    strategy_details=item['strategy_details']
                )

        self.stdout.write(self.style.SUCCESS('Data successfully populated'))
