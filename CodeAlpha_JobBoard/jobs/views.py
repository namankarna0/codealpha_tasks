from rest_framework import viewsets, permissions, status, parsers
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Employer, Candidate, JobListing, Resume, Application
from .serializers import (
    EmployerSerializer, CandidateSerializer, JobListingSerializer, 
    ResumeSerializer, ApplicationSerializer
)

class EmployerViewSet(viewsets.ModelViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    permission_classes = [permissions.IsAuthenticated]

class JobListingViewSet(viewsets.ModelViewSet):
    queryset = JobListing.objects.all().order_by('-created_at')
    serializer_class = JobListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """Custom logic for Job Search Filters"""
        queryset = JobListing.objects.all().order_by('-created_at')
        
        # 1. Filter by location (e.g., ?location=Kathmandu)
        location = self.request.query_params.get('location')
        if location:
            queryset = queryset.filter(location__icontains=location)
            
        # 2. Filter by job type (e.g., ?job_type=full_time)
        job_type = self.request.query_params.get('job_type')
        if job_type:
            queryset = queryset.filter(job_type=job_type)

        # 3. Search by title/description (e.g., ?search=developer)
        search = self.request.query_params.get('search')
        if search:
            queryset = queryset.filter(title__icontains=search) | queryset.filter(description__icontains=search)

        return queryset

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def apply(self, request, pk=None):
        """Custom endpoint to apply for a job"""
        job = self.get_object()
        
        # Check if user already has a candidate profile
        try:
            candidate = request.user.candidate
        except Candidate.DoesNotExist:
            return Response({"error": "Please create a candidate profile first."}, status=status.HTTP_400_BAD_REQUEST)

        resume_id = request.data.get('resume')
        if not resume_id:
            return Response({"error": "A resume must be attached to apply."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            resume = Resume.objects.get(id=resume_id, candidate=candidate)
        except Resume.DoesNotExist:
            return Response({"error": "Resume not found or does not belong to you."}, status=status.HTTP_404_NOT_FOUND)

        # Prevent double applications
        if Application.objects.filter(job=job, candidate=candidate).exists():
            return Response({"error": "You have already applied for this job."}, status=status.HTTP_400_BAD_REQUEST)

        # Create the application
        Application.objects.create(job=job, candidate=candidate, resume=resume)
        return Response({"message": "Application submitted successfully!"}, status=status.HTTP_201_CREATED)

class ResumeViewSet(viewsets.ModelViewSet):
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (parsers.MultiPartParser, parsers.FormParser) # Allows file uploads

    def get_queryset(self):
        # Users can only see their own resumes
        return Resume.objects.filter(candidate__user=self.request.user)

    def perform_create(self, serializer):
        # Auto-create candidate profile if it doesn't exist
        candidate, created = Candidate.objects.get_or_create(user=self.request.user)
        serializer.save(candidate=candidate)

class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Employers see applications for their jobs, Candidates see their own
        user = self.request.user
        if hasattr(user, 'employer'):
            return Application.objects.filter(job__employer=user.employer)
        return Application.objects.filter(candidate__user=user)