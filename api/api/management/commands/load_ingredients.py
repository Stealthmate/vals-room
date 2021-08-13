
import yaml

from django.db import transaction
from django.core.management.base import BaseCommand
from django.utils import timezone

from api.models.drinks import DrinkIngredient, Ingredient

class Command(BaseCommand):
    help = 'Load YAML ingredient list into DB'

    def add_arguments(self, parser):
        parser.add_argument('FILE', type=str, help='Path to YAML file containing ingredients')

    def handle(self, *args, **kwargs):
        f = kwargs['FILE']
        items = []
        with open(f, 'r') as stream:
            try:
                items = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                self.stdout.write(self.style.ERROR('File coud not be parsed'))

        objs = [
            Ingredient(
                **{
                    **i,
                    'abv': i.get('abv', 0)
                }
            ) for i in items
        ]
        with transaction.atomic():
            DrinkIngredient.objects.all().delete()
            Ingredient.objects.all().delete()
            Ingredient.objects.bulk_create(objs)
