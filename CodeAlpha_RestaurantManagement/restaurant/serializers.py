from rest_framework import serializers
from .models import MenuItem, InventoryItem, Table, Reservation, Order, OrderItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    customer = serializers.ReadOnlyField(source='customer.username')
    
    class Meta:
        model = Reservation
        fields = ['id', 'customer', 'table', 'reservation_time', 'number_of_guests', 'status']
        read_only_fields = ['status']

class OrderItemSerializer(serializers.ModelSerializer):
    menu_item_name = serializers.ReadOnlyField(source='menu_item.name')
    
    class Meta:
        model = OrderItem
        fields = ['id', 'menu_item', 'menu_item_name', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.ReadOnlyField(source='customer.username')
    items = OrderItemSerializer(source='order_items', many=True, read_only=True)
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = ['id', 'customer', 'table', 'status', 'created_at', 'items', 'total_price']
        read_only_fields = ['status']