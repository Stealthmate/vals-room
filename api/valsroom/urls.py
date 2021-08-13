from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from api.views import users as views_users
from api.views import drinks as views_drinks
from api.views import orders as views_orders

router = routers.DefaultRouter()

router.register(r'admin/invitations', views_users.UserInvitationViewSet, basename='invitations')

router.register(r'drinks', views_drinks.DrinkViewSet, basename='drinks')
router.register(r'tags', views_drinks.TagViewSet, basename='tag')
router.register(r'orders', views_orders.OrderViewSet, basename='orders')
router.register(r'users', views_users.UserViewSet, basename='user')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='auth'),
    path('', include(router.urls))
]