import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    help = 'Import phones from CSV file'

    def add_arguments(self, parser):
        parser.add_argument(
            'csv_file', 
            type=str, 
            help='phones.csv' # C:\python\django 1\dj-homeworks\2.1-databases\work_with_database\
            )

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            phone_b = Phone()
            phone_b.name = phone['name']
            phone_b.price = phone['price']
            phone_b.image = phone['image']
            phone_b.release_date = phone['release_date']
            phone_b.lte_exists = phone['lte_exists']

            phone_b.save()

        self.stdout.write(self.style.SUCCESS('Phones imported successfully!'))
