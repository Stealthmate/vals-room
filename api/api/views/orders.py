
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, mixins, serializers, status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models.orders import Order

from api.services.orders import OrdersService
from api.serializers.orders import PlaceOrderSerializer, DetailedOrderSerializer, SimpleOrderSerializer

class OrderViewSet(
        viewsets.GenericViewSet
    ):
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'pk'

    @property
    def service(self):
        return OrdersService(self.request.user)

    def list(self, request):
        return Response(DetailedOrderSerializer(
            self.service.list_active_orders(),
            many=True
        ).data)

    def destroy(self, request, pk=None):
        self.service.service_for(int(pk)).cancel()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request):
        s = PlaceOrderSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        vdata = s.validated_data
        self.service.place_order(vdata['drink'])
        return Response(status=status.HTTP_201_CREATED)

    @action(methods=['GET'], detail=False, url_path='user')
    def list_user_orders(self, request):
        return Response(SimpleOrderSerializer(self.service.list_user_orders(), many=True).data)

    @action(methods=['POST'], detail=True, url_path='complete')
    def complete(self, request, pk=None):
        self.service.service_for(int(pk)).complete()
        return Response()

    @action(methods=['GET'], detail=False, url_path='completed')
    def list_completed(self, request):return Response(DetailedOrderSerializer(
            self.service.list_completed_orders(),
            many=True
        ).data)

    @action(methods=['POST'], detail=True, url_path='pay')
    def pay(self, request, pk=None):
        self.service.service_for(int(pk)).pay()
        return Response()
