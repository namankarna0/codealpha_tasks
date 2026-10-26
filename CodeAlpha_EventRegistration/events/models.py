from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    """Custom user model to differentiate organizers and attendees."""
    is_organizer = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_events')
    
    def __str__(self):
        return self.title
    
    @property
    def spaces_left(self):
        # Calculates how many spots are left based on registrations
        registered_count = self.registrations.count()
        return max(0, self.capacity - registered_count)

class Registration(models.Model):
    """Links a user to an event."""
    STATUS_CHOICES = (
        ('registered', 'Registered'),
        ('cancelled', 'Cancelled'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registrations')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='registered')
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # A user can only have ONE registration per event
        unique_together = ('user', 'event')

    def __str__(self):
        return f"{self.user.username} -> {self.event.title}"
