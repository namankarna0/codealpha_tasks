from django.db import models
from django.contrib.auth.models import User

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    stock_quantity = models.PositiveIntegerField(default=0)
    unit = models.CharField(max_length=20, default='kg') # e.g., kg, liters, pieces

    def __str__(self):
        return f"{self.name} ({self.stock_quantity} {self.unit})"

class Table(models.Model):
    table_number = models.CharField(max_length=10, unique=True)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"Table {self.table_number} (Seats {self.capacity})"

class Reservation(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    reservation_time = models.DateTimeField()
    number_of_guests = models.PositiveIntegerField()
    status = models.CharField(max_length=20, default='confirmed') # confirmed, cancelled

    def __str__(self):
        return f"{self.customer.username} - Table {self.table.table_number} at {self.reservation_time}"

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('preparing', 'Preparing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.status}"

    @property
    def total_price(self):
        # Calculates total dynamically based on items ordered
        return sum(item.total_price for item in self.order_items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return self.menu_item.price * self.quantity

    def __str__(self):
        return f"{self.quantity}x {self.menu_item.name}"