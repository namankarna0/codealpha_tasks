# Task 1: URL Shortener (Flask)

A RESTful API that converts long URLs into short, unique codes, built as part of the CodeAlpha Backend Internship.

## 🚀 Features
- **Shorten URLs:** Accepts long URLs and returns a unique 7-character base62 short code.
- **Redirects:** Accessing the short URL redirects (HTTP 302) the user to the original URL.
- **Click Analytics:** Tracks the number of times each short link is clicked.
- **Collision Safety:** Uses cryptographic randomness (`secrets`) combined with database unique constraints and a retry loop to guarantee 100% unique codes.
- **Security:** Validates URLs strictly to `http/https` to prevent open-redirects and XSS attacks (blocks schemes like `javascript:`).

## 🛠️ Tech Stack
- **Framework:** Flask
- **Database:** SQLite with SQLAlchemy (ORM)
- **Architecture:** App factory pattern with separation of concerns (Routes, Services, Models).
- **Testing:** Pytest (Unit & Integration tests).

## ⚙️ Local Setup Instructions

1. **Clone the repository and navigate to this folder:**
   ```bash
   cd CodeAlpha_URLShortener

2.  Create and activate a virtual environment:

bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
Install dependencies:

bash
pip install -r requirements.txt
Run the development server:

bash
python run.py
The app will be available at http://127.0.0.1:5000/.

🧪 Running Tests
To run the automated unit tests and verify the logic:

bash
python -m pytest -v
🔌 API Endpoints
Method	Endpoint	Description	Payload Example
GET	/	View the frontend UI to shorten links	N/A
POST	/api/shorten	Generate a short code for a long URL	{"url": "https://example.com/long/path"}
GET	/<code>	Redirects to the original URL

💻 Frontend Demo
The app includes a clean HTML/JS frontend. When you visit http://127.0.0.1:5000/, you can paste a URL, click "Shorten", and use the "Copy Link" button to instantly copy the shortened URL to your clipboard.