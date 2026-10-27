from django.shortcuts import render
from rest_framework import viewsets, permissions, status, serializers
from rest_framework.response import Response
from .models import MenuItem, InventoryItem, Table, Reservation, Order, OrderItem
from .serializers import MenuItemSerializer, InventoryItemSerializer, TableSerializer, ReservationSerializer, OrderSerializer, OrderItemSerializer
from rest_framework.decorators import action
from django.utils import timezone
from datetime import timedelta




# Create your views here.

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated]

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # 1. Check table capacity
        table = serializer.validated_data['table']
        guests = serializer.validated_data['number_of_guests']
        if guests > table.capacity:
            raise serializers.ValidationError(f"Table only seats {table.capacity} people.")
            
        # 2. Check table availability (3-hour window)
        req_time = serializer.validated_data['reservation_time']
        # Check if there is a reservation for this table within 3 hours of the requested time
        conflict = Reservation.objects.filter(
            table=table, 
            status='confirmed',
            reservation_time__range=(req_time - timedelta(hours=3), req_time + timedelta(hours=3))
        ).exists()

        if conflict:
            raise serializers.ValidationError("Table is already booked around this time.")
            
        # If we pass the checks, save the reservation
        serializer.save(customer=self.request.user)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

    @action(detail=True, methods=['post'])
    def add_item(self, request, pk=None):
        """Add an item to an order and update inventory automatically."""
        order = self.get_object()
        menu_item_id = request.data.get('menu_item')
        quantity = int(request.data.get('quantity', 1))

        try:
            menu_item = MenuItem.objects.get(id=menu_item_id)
        except MenuItem.DoesNotExist:
            return Response({"error": "Menu item not found"}, status=status.HTTP_404_NOT_FOUND)

        # --- INVENTORY AUTO-UPDATE LOGIC (Mock Example) ---
        # In a real app, MenuItem would have a Recipe mapping to InventoryItems.
        # For this task, let's just assume if the name contains "Burger", it uses "Beef Patty"
        if "Burger" in menu_item.name:
            try:
                patty = InventoryItem.objects.get(name="Beef Patty")
                if patty.stock_quantity < quantity:
                    return Response({"error": f"Not enough Beef Patty in stock. Only {patty.stock_quantity} left."}, status=status.HTTP_400_BAD_REQUEST)
                patty.stock_quantity -= quantity
                patty.save()
            except InventoryItem.DoesNotExist:
                pass # If inventory item isn't tracked, skip

        # Add item to order
        order_item, created = OrderItem.objects.get_or_create(
            order=order, menu_item=menu_item, defaults={'quantity': quantity}
        )
        
        if not created:
            order_item.quantity += quantity
            order_item.save()

        return Response({"message": "Item added successfully", "order_total": order.total_price}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        """Mark order as completed."""
        order = self.get_object()
        order.status = 'completed'
        order.save()
        return Response({"message": "Order completed successfully"})