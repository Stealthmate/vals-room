
from rest_framework import serializers

from api.models.drinks import Drink, Tag, DrinkIngredient
from api.models.orders import Order

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'id',
            'name'
        ]

class DrinkIngredientSerializer(serializers.Serializer):
    name = serializers.CharField(source='ingredient.name')
    amount = serializers.IntegerField()

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = [ 'id', 'name', 'abv', 'stars', 'tags' ]
    stars = serializers.IntegerField()
    tags = serializers.ListSerializer(child=TagSerializer())
