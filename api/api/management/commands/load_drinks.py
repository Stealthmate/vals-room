
import yaml

from django.db import transaction
from django.core.management.base import BaseCommand
from django.utils import timezone

from api.models import Drink, DrinkIngredient, Ingredient

class Command(BaseCommand):
    help = 'Load YAML drink list into DB'

    def add_arguments(self, parser):
        parser.add_argument('FILE', type=str, help='Path to YAML file containing drinks')

    def handle(self, *args, **kwargs):
        f = kwargs['FILE']
        items = []
        with open(f, 'r') as stream:
            try:
                items = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                self.stdout.write(self.style.ERROR('File coud not be parsed'))

        with transaction.atomic():
            Drink.objects.all().delete()
            DrinkIngredient.objects.all().delete()
            for item in items:
                ings = []
                for i in item['ingredients']:
                    ing, amt = i.split(',')
                    amt = int(amt)
                    ings.append((ing, amt))

                dings = []
                for name, amount in ings:
                    try:
                        ing = Ingredient.objects.get(name=name)
                        dings.append(DrinkIngredient.objects.get_or_create(ingredient=ing, amount=amount)[0])
                    except Ingredient.DoesNotExist:
                        self.stdout.write(self.style.ERROR(f'Could not find ingredient: {name}'))
                        raise Ingredient.DoesNotExist()
                d = Drink.objects.create(
                    name=item['name'],
                    japanese_name=item['name'], # TODO
                )
                d.ingredients.add(*dings)