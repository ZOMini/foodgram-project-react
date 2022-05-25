import json

from django.core.management.base import BaseCommand

from backend.api.models import Ingredient


class Command(BaseCommand):
    help = 'Uploading Ingredients data-set'

    def handle(self, *args, **options):
        with open(
                './ingredients.json', encoding='utf-8'
        ) as json_file:
            ingredients = json.load(json_file)
            for ingredient in ingredients:
                name, measurement_unit = ingredient['name'], ingredient['measurement_unit']
                Ingredient.objects.get_or_create(
                    name=name,
                    measurement_unit=measurement_unit
                )

if __name__ == "__main__":
    app = Command()
    app.handle()

# в shell проекта, пилим это:
# from import_json import Command
# app=Command()
# app.handle()
