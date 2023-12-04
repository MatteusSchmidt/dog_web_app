from django.core.management.base import BaseCommand
import json
from animals.models import CatModel


# functions to create a terminal command to inject JSON data printed in the clean_json_cats file into the sqlite db
class Command(BaseCommand):
    help = 'Import data for cats from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file to import')

    def handle(self, *args, **kwargs):
        json_file_path = kwargs['json_file']

        with open(json_file_path, 'r') as file:
            data = json.load(file)

        # writes in data for each instance of a cat
        for item in data:
            cat_instance = CatModel(
                weight=item.get('weight', {'imperial': None, 'metric': None}),
                name=item.get('name', ''),
                cfa_url=item.get('cfa_url', ''),
                vetstreet_url=item.get('vetstreet_url', ''),
                vcahospitals_url=item.get('vcahospitals_url', ''),
                temperament=item.get('temperament', ''),
                origin=item.get('origin', ''),
                country_codes=item.get('country_codes', ''),
                country_code=item.get('country_code', ''),
                description=item.get('description', ''),
                life_span=item.get('life_span', ''),
                wikipedia_url=item.get('wikipedia_url', ''),
                reference_image_id=item.get('reference_image_id', ''),
                left=item.get('left', []),
                image_url=item.get('image_url', ''),
                stars=item.get('stars', []),
            )
            cat_instance.save()

        self.stdout.write(self.style.SUCCESS('Cat data imported successfully'))
