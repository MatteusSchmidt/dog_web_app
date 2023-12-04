from django.core.management.base import BaseCommand
import json
from animals.models import DogModel


# functions to create a terminal command to inject JSON data printed in the clean_json_dogs file into the sqlite db
class Command(BaseCommand):
    help = 'Import data from a JSON file into the database'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file to import')

    def handle(self, *args, **kwargs):
        json_file_path = kwargs['json_file']

        with open(json_file_path, 'r') as file:
            data = json.load(file)

        # writes in data for each instance of a dog
        for item in data:
            dog_instance = DogModel(
                weight=item.get('weight', {'imperial': None, 'metric': None}),
                height=item.get('height', {'imperial': None, 'metric': None}),
                name=item.get('name', ''),
                description=item.get('description', ''),
                country_code=item.get('country_code', ''),
                bred_for=item.get('bred_for', ''),
                breed_group=item.get('breed_group', ''),
                life_span=item.get('life_span', ''),
                history=item.get('history', ''),
                temperament=item.get('temperament', ''),
                origin=item.get('origin', ''),
                reference_image_id=item.get('reference_image_id', ''),
                image=item.get('image', {'id': None, 'width': None, 'height': None, 'url': None}),
            )
            dog_instance.save()

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
