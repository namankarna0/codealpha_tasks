from django.contrib import admin
from .models import Employer, Candidate, JobListing, Resume, Application

admin.site.register(Employer)
admin.site.register(Candidate)
admin.site.register(JobListing)
admin.site.register(Resume)
admin.site.register(Application)