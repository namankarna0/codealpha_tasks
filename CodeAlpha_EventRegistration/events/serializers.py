from rest_framework import serializers
from .models import Event, Registration

class EventSerializer(serializers.ModelSerializer):
    spaces_left = serializers.ReadOnlyField()
    organizer = serializers.ReadOnlyField(source='organizer.username')

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'location', 'capacity', 'spaces_left', 'organizer']

class RegistrationSerializer(serializers.ModelSerializer):
    event_title = serializers.ReadOnlyField(source='event.title')
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Registration
        fields = ['id', 'user', 'event', 'event_title', 'status', 'registered_at']
        read_only_fields = ['status']