
from django.db import models

from api.models.base import BaseModel
from api.models.users import ValsRoomUser
from api.models.drinks import Drink

class Order(BaseModel):
    user = models.ForeignKey(ValsRoomUser, on_delete=models.PROTECT)
    drink = models.ForeignKey(Drink, on_delete=models.PROTECT)
    done = models.BooleanField(default=False)

    created_at = models.DateTimeField()

class Sale(BaseModel):
    user_name = models.CharField(max_length=255)
    drink_name = models.CharField(max_length=255)
    base_price = models.IntegerField()
    sale_price = models.IntegerField()
    created_at = models.DateTimeField()