import os
import django
from faker import Faker
from core.models import Crime, Location
from django.utils import timezone

def setup_django():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'heatmapAPI.settings')
    django.setup()

def generate_dummy_crime_data(num_records=10):
    fake = Faker()

    # Assuming you have some locations already in your database
    locations = Location.objects.all()

    for _ in range(num_records):
        crime = Crime.objects.create(
            type_of_crime=fake.word(),
            description_of_crime=fake.sentence(),
            date_of_crime=fake.date_this_decade(),
            location=fake.random_element(locations),
        )
        print(f"Created Crime: {crime}")

if __name__ == '__main__':
    setup_django()
    generate_dummy_crime_data()