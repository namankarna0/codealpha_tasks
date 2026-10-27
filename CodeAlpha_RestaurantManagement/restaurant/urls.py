from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet, InventoryViewSet, TableViewSet, ReservationViewSet, OrderViewSet


router = DefaultRouter()
router.register(r'menu', MenuItemViewSet)
router.register(r'inventory', InventoryViewSet)
router.register(r'tables', TableViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]