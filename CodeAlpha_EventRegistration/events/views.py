from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

from .models import Event, Registration
from .serializers import EventSerializer, RegistrationSerializer

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # Bypass CSRF for API testing

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('date')
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [BasicAuthentication] 


    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def register(self, request, pk=None):
        event = self.get_object()
        
        if event.spaces_left <= 0:
            return Response({"error": "Event is full"}, status=status.HTTP_400_BAD_REQUEST)

        registration, created = Registration.objects.get_or_create(
            user=request.user, 
            event=event,
            defaults={'status': 'registered'}
        )

        if not created:
            if registration.status == 'registered':
                return Response({"error": "You are already registered for this event"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                registration.status = 'registered'
                registration.save()
                return Response({"message": "Registration re-activated successfully"})

        return Response({"message": "Successfully registered for the event"}, status=status.HTTP_201_CREATED)

class RegistrationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [CsrfExemptSessionAuthentication] # <--- ADD THIS HERE TOO

    def get_queryset(self):
        return Registration.objects.filter(user=self.request.user)

    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        registration = self.get_object()
        registration.status = 'cancelled'
        registration.save()
        return Response({"message": "Registration cancelled successfully"})

def event_frontend(request):
    return render(request, 'events/event_list.html')