import json

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, mixins, serializers
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Drink, Tag, Order, DrinkIngredient

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'id',
            'name'
        ]

class TagViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = [ IsAuthenticated ]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = [ 'id', 'name', 'abv', 'stars', 'tags' ]
    stars = serializers.IntegerField()
    tags = serializers.ListSerializer(child=TagSerializer())

class DrinkIngredientSerializer(serializers.Serializer):
    name = serializers.CharField(source='ingredient.name')
    amount = serializers.IntegerField()

class DrinkRecipeSerializer(serializers.Serializer):
    name = serializers.CharField()
    ingredients = serializers.ListSerializer(child=DrinkIngredientSerializer())

class DrinkViewSet(
        mixins.ListModelMixin,
        viewsets.GenericViewSet
    ):
    permission_classes = [IsAuthenticated]
    serializer_class = DrinkSerializer
    queryset = Drink.objects.all()

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        read_only_fields = [ 'id', 'recipe' ]
        fields = [
            *read_only_fields,
            'name',
            'drink'
        ]
    recipe = DrinkRecipeSerializer(source='drink', read_only=True) 

class OrderViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = [ IsAuthenticated ]
    queryset = Order.objects.filter(done=False)
    serializer_class = OrderSerializer

    @action(methods=['PUT'], detail=True, url_path='complete')
    def complete(self, request, pk=None):
        o = self.get_object()
        o.done = True
        o.save()
        return Response()
    
    @action(methods=['DELETE'], detail=True, url_path='')
    def cancel(self, request, pk=None):
        self.get_object().delete()
        return Response()

class ManageViewSet(viewsets.GenericViewSet):
    pass

class UserViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    @action(methods=['GET'], detail=False, url_name='me', url_path='me')
    def me(self, request):
        return Response({ 'username': request.user.username })