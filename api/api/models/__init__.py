import math

from django.db import models

class BaseModel(models.Model):
    class Meta:
        abstract = True
    id = models.AutoField(primary_key=True)

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

    @property
    def price(self):
        return sum(x.price for x in self.ingredients.all())

    @property
    def stars(self):
        return int(math.ceil((self.price + 50) / 100))

    @property
    def abv(self):
        ings = self.ingredients.all()
        return sum(x.ingredient.abv * x.amount for x in ings) / sum(x.amount for x in ings)

class Order(BaseModel):
    name = models.TextField()
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)