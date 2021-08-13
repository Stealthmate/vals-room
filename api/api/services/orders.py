
from django.utils import timezone
from django.db import transaction

from api.models.orders import Order, Sale
from api.models.drinks import Drink

from api.services.users import UserService
from api.services.permissions import withStaff

class OrderService(UserService):
    def __init__(self, user, order):
        super().__init__(user)
        self.order = order

    @withStaff
    def cancel(self):
        self.order.delete()

    @withStaff
    def complete(self):
        self.order.done = True
        self.order.save()

    @withStaff
    def pay(self):
        with transaction.atomic():
            Sale.objects.create(
                user_name=self.order.user.django_user.first_name,
                drink_name=self.order.drink.name,
                base_price=self.order.drink.price,
                sale_price=self.order.drink.stars * 100,
                created_at=timezone.now()
            )
            self.order.delete()

class OrdersService(UserService):
    @withStaff
    def list_active_orders(self):
        return Order.objects.filter(done=False)

    @withStaff
    def list_completed_orders(self):
        return Order.objects.filter(done=True)

    def list_user_orders(self):
        return Order.objects.filter(done=False, user=self.user)

    def place_order(self, drink_id):
        return Order.objects.create(
            user=self.user,
            drink=Drink.objects.get(id=drink_id),
            created_at=timezone.now()
        )

    def service_for(self, order_id):
        return OrderService(self.user.django_user, Order.objects.get(id=order_id))

