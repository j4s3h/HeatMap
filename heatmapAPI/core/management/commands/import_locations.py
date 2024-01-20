from django.core.management.base import BaseCommand ,CommandError
import pandas as pd
import chardet
from core.models import Location  # Adjust the import based on your actual model location

class Command(BaseCommand):
    help = 'Import locations from CSV file using Pandas'

    def handle(self, *args, **options):
        csv_file_path = 'cabanatuanbarangay.csv'

        # Use 'rb' mode for Python 2.x, 'r' for Python 3.x
        with open(csv_file_path, 'rb') as f:
            result = chardet.detect(f.read())

        try:
            df = pd.read_csv(csv_file_path, encoding=result['encoding'])
        except pd.errors.EmptyDataError:
            raise CommandError('CSV file is empty')

        for index, row in df.iterrows():
            try:
                location_id = int(row['location_id'])
                location_name = row['location_name']
                latitude = float(row['latitude'])  # Convert to float
                longitude = float(row['longitude'])  # Convert to float
            except (ValueError, KeyError) as e:
                raise CommandError(f'Error parsing data in row {index + 2}: {e}')

            try:
                location, created = Location.objects.get_or_create(
                    location_id=location_id,
                    defaults={
                        'location_name': location_name,
                        'latitude': latitude,
                        'longitude': longitude,
                    }
                )

                if not created:
                    location.location_name = location_name
                    location.latitude = latitude
                    location.longitude = longitude
                    location.save()

                self.stdout.write(self.style.SUCCESS(f'Successfully imported {location_name}'))
            except Exception as e:
                raise CommandError(f'Error saving data in row {index + 2}: {e}')