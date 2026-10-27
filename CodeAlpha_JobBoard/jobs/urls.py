from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployerViewSet, JobListingViewSet, ResumeViewSet, ApplicationViewSet


router = DefaultRouter()
router.register(r'employers', EmployerViewSet)
router.register(r'jobs', JobListingViewSet)

# Add basename to the viewsets that use custom get_queryset() methods
router.register(r'resumes', ResumeViewSet, basename='resume')
router.register(r'applications', ApplicationViewSet, basename='application')

urlpatterns = [
    path('', include(router.urls)),
]