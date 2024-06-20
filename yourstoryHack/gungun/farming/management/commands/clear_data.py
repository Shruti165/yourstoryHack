# farming/management/commands/clear_data.py

from django.core.management.base import BaseCommand
from farming.models import WeatherData, MarketData, FarmStrategy

class Command(BaseCommand):
    help = 'Clear all data from specific models'

    def handle(self, *args, **options):
        WeatherData.objects.all().delete()
        MarketData.objects.all().delete()
        FarmStrategy.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('All data cleared successfully'))
