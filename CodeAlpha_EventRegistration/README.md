# Task 2: Event Registration System (Django)

A full-stack backend API and frontend for managing events and user registrations, built as part of the CodeAlpha Backend Internship.

## 🚀 Features
- **Custom User Model:** Extends Django's default user to distinguish between event organizers and attendees.
- **Event Management:** Create, view, and manage events with defined capacities.
- **Smart Capacity Tracking:** Automatically calculates `spaces_left` based on active registrations.
- **Secure Registration Flow:** 
  - Prevents overbooking (blocks registration if the event is full).
  - Prevents duplicate registrations (a user can only register once).
  - Allows users to cancel and re-activate their spot.
- **Frontend Interface:** A responsive UI built with HTML/JS that connects to the REST API.

## 🛠️ Tech Stack
- **Framework:** Django & Django REST Framework (DRF)
- **Database:** SQLite (default Django database)
- **Authentication:** Basic Auth (for API) & Session Auth (for frontend)

## ⚙️ Local Setup Instructions

1. **Clone the repository and navigate to this folder:**
   ```bash
   cd CodeAlpha_EventRegistration

2. Create and activate a virtual environment:

bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
Install dependencies:

bash
pip install -r requirements.txt
Apply database migrations:

bash
python manage.py makemigrations
python manage.py migrate
Create an admin account (for testing):

bash
python manage.py createsuperuser
(Follow the prompts to set a username and password).

3. Run the development server:

bash
python manage.py runserver
🧪 API Endpoints
You can test these endpoints using the browsable API in your browser, or tools like Postman/Thunder Client.

Method	Endpoint	Description	Auth Required
GET	/api/events/	List all events	No
POST	/api/events/	Create a new event	Yes
POST	/api/events/<id>/register/	Register for a specific event	Yes
GET	/api/my-registrations/	View your own registrations	Yes
POST	/api/my-registrations/<id>/cancel/	Cancel a registration	Yes
💻 Frontend Demo
To view the interactive frontend:

Start the server.

Go to http://127.0.0.1:8000/api/frontend/

Ensure you are logged in (you can log in via http://127.0.0.1:8000/api/events/ top right corner).

Click "Register Now" to test the logic!


