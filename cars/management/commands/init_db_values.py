from django.core.management.base import BaseCommand
from cars.models import Car
from reviews.enum import Rating
from reviews.models import Reviews

class Command(BaseCommand):
    help = 'Populates the database with initial data'

    def handle(self, *args, **kwargs):
        if Car.objects.all().exists():
            return
        products = [
            {"name": "LiXiang L6 Pro", "price": 45000},
            {"name": "NIO ET7", "price": 30000},
            {"name": "BYD Song Plus", "price": 35000},
            {"name": "Kia Soul EV", "price": 35000},
            {"name": "XPeng P7", "price": 45000},
            {"name": "BYD Tang EV", "price": 50000},
            {"name": "SAIC MG ZS EV", "price": 55000},
            {"name": "DongFeng Box", "price": 45000},
            {"name": "DongFeng Mage", "price": 45000},
            {"name": "AITO M7", "price": 45000},
            {"name": "AITO M9", "price": 45000},
            {"name": "BYD Han", "price": 45000},
            {"name": "Tesla Model 3", "price": 45000},
            {"name": "Tesla Model Y", "price": 45000},
            {"name": "Xpeng P7", "price": 45000},
            {"name": "Xpeng MONA M03", "price": 45000},
            {"name": "Denza N7", "price": 45000},
        ]
        for item in products:
            Car.objects.create(name=item['name'], price=item['price'])

        products = [
            {"name": "Аня", "review": "Лучший сайт в мире", "rating": Rating.FIVE},
            {"name": "Дима", "review": "Как же быстро работает сайт", "rating": Rating.FIVE},
            {"name": "Никита", "review": "Очень вкусные цены", "rating": Rating.FIVE},
        ]
        for item in products:
            Reviews.objects.create(name=item['name'], review=item['review'], rating=item['rating'])