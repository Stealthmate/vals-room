
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, mixins, serializers
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models.drinks import Drink, Tag, DrinkIngredient
from api.models.orders import Order

from api.serializers.drinks import TagSerializer, DrinkSerializer

from api.services.drinks import DrinksService

class TagViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = [ IsAuthenticated ]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class DrinkViewSet(
        mixins.ListModelMixin,
        viewsets.GenericViewSet
    ):
    permission_classes = [IsAuthenticated]
    serializer_class = DrinkSerializer

    def list(self, request):
        return Response(self.serializer_class(
            DrinksService(request.user).list_drinks(),
            many=True
        ).data)
