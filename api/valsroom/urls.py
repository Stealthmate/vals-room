from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from api import views as api_views

router = routers.DefaultRouter()
router.register(r'drinks', api_views.DrinkViewSet, basename='drinks')
router.register(r'orders', api_views.OrderViewSet, basename='orders')
router.register(r'manage', api_views.ManageViewSet, basename='manage')
router.register(r'users', api_views.UserViewSet, basename='user')
router.register(r'tags', api_views.TagViewSet, basename='tag')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='auth'),
    path('', include(router.urls))
]