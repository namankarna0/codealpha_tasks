# Task 4: Job Board Platform (Django)

A comprehensive backend API for a job board platform, allowing employers to post jobs and candidates to apply with uploaded resumes.

## 🚀 Features
- **Job Listings:** Employers can create job posts with titles, descriptions, locations, and salaries.
- **Advanced Search Filters:** Users can search jobs by keyword (`?search=developer`), location (`?location=Kathmandu`), and job type (`?job_type=full_time`).
- **Resume Uploads:** Candidates can securely upload PDF/image resumes using Django's `MultiPartParser`.
- **Application Tracking:** Candidates can apply for jobs, attaching a specific resume. 
- **Anti-Spam Logic:** Prevents candidates from applying to the same job twice.
- **Role-based views:** Employers can see applications for their jobs, while candidates can see their own submitted applications.

## 🛠️ Tech Stack
- **Framework:** Django & Django REST Framework (DRF)
- **Database:** SQLite
- **File Handling:** Django Media Files (Pillow)

## ⚙️ Local Setup Instructions

1. **Navigate to this folder:**
   ```bash
   cd CodeAlpha_JobBoard

2. Create and activate a virtual environment:

bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
Install dependencies:

bash
pip install -r requirements.txt
Apply database migrations:

bash
python manage.py migrate
Create an admin account:

bash
python manage.py createsuperuser
Run the server:

bash
python manage.py runserver
🧪 API Endpoints
Method	Endpoint	Description
GET/POST	/api/jobs/	List all jobs or create a new job
GET	/api/jobs/?search=<keyword>	Search jobs by title or description
GET	/api/jobs/?location=<city>	Filter jobs by location
POST	/api/jobs/<id>/apply/	Apply for a job (Requires resume ID)
GET/POST	/api/resumes/	List or upload a resume (Multipart form)
GET	/api/applications/	View your applications (or received applications if employer)
