from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, RegistrationViewSet, event_frontend

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'my-registrations', RegistrationViewSet, basename='my-registrations')

urlpatterns = [
    path('frontend/', event_frontend, name='event-frontend'),
    path('', include(router.urls)),
]