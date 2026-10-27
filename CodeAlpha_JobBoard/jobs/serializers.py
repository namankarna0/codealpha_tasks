from rest_framework import serializers
from .models import Employer, Candidate, JobListing, Resume, Application

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'

class JobListingSerializer(serializers.ModelSerializer):
    employer_name = serializers.ReadOnlyField(source='employer.company_name')

    class Meta:
        model = JobListing
        fields = ['id', 'employer', 'employer_name', 'title', 'description', 'location', 'salary', 'job_type', 'created_at']

class ResumeSerializer(serializers.ModelSerializer):
    candidate_name = serializers.ReadOnlyField(source='candidate.user.username')
    
    class Meta:
        model = Resume
        fields = ['id', 'candidate', 'candidate_name', 'file', 'uploaded_at']
        read_only_fields = ['candidate']

class ApplicationSerializer(serializers.ModelSerializer):
    job_title = serializers.ReadOnlyField(source='job.title')
    candidate_name = serializers.ReadOnlyField(source='candidate.user.username')

    class Meta:
        model = Application
        fields = ['id', 'job', 'job_title', 'candidate', 'candidate_name', 'resume', 'status', 'applied_at']
        read_only_fields = ['candidate']