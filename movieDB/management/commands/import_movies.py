import csv
from django.core.management.base import BaseCommand
from movieDB.models import Movie

class Command(BaseCommand):
    help = 'Replace movies in the database with data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']

        # Clear existing movies
        Movie.objects.all().delete()

        # Open and read the CSV file
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Create a Movie instance and save it to the database
                Movie.objects.create(**row)

        self.stdout.write(self.style.SUCCESS('Successfully replaced movies in the database'))
