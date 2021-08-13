
from rest_framework import serializers

from api.models.drinks import Drink, Tag, DrinkIngredient
from api.models.orders import Order

from api.serializers.drinks import DrinkIngredientSerializer
from api.serializers.users import ValsRoomUserSerializer

class PlaceOrderSerializer(serializers.Serializer):
    drink = serializers.IntegerField()

class DrinkRecipeSerializer(serializers.Serializer):
    name = serializers.CharField()
    ingredients = serializers.ListSerializer(child=DrinkIngredientSerializer())

class DetailedOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [ 'id', 'user', 'drink', 'recipe', 'stars' ]
    user = ValsRoomUserSerializer()
    stars = serializers.IntegerField(source='drink.stars')
    recipe = DrinkRecipeSerializer(source='drink')

class SimpleOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [ 'name', 'stars' ]
    name = serializers.CharField(source='drink.name')
    stars = serializers.IntegerField(source='drink.stars')