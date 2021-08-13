import math

from django.db import models

from api.models.base import BaseModel

class Ingredient(BaseModel):
    name = models.TextField()
    content = models.IntegerField()
    price = models.IntegerField()
    abv = models.IntegerField()

class DrinkIngredient(BaseModel):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    amount = models.IntegerField()

    @property
    def price(self):
        return self.ingredient.price * self.amount / self.ingredient.content

class Tag(BaseModel):
    name = models.TextField()

class Drink(BaseModel):
    name = models.TextField()
    japanese_name = models.TextField()
    ingredients = models.ManyToManyField(DrinkIngredient)
    tags = models.ManyToManyField(Tag)
    stars = models.IntegerField()

    @property
    def price(self):
        return sum(x.price for x in self.ingredients.all())

    @property
    def abv(self):
        ings = self.ingredients.all()
        return sum(x.ingredient.abv * x.amount for x in ings) / sum(x.amount for x in ings)
