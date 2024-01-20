from django.core.management.base import BaseCommand
from faker import Faker
from core.models import Crime, Location

class Command(BaseCommand):
    help = 'Generate dummy data for the Crime model'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Assuming you have some locations already in your database
        locations = Location.objects.all()

        num_records = int(input('Enter the number of dummy records to create: '))

        for _ in range(num_records):
            crime = Crime.objects.create(
                type_of_crime=fake.word(),
                description_of_crime=fake.sentence(),
                date_of_crime=fake.date_this_decade(),
                location=fake.random_element(locations),
            )
            self.stdout.write(self.style.SUCCESS(f"Created Crime: {crime}"))