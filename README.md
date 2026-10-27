# CodeAlpha Backend Development Internship Tasks

Welcome to my repository for the CodeAlpha Backend Development Internship. This repository contains full-stack backend projects built from scratch, demonstrating RESTful API design, database modeling, secure authentication, and custom business logic.

## 📂 Projects Overview

| Task | Project | Tech Stack | Directory |
| :--- | :--- | :--- | :--- |
| **1** | **URL Shortener** | Flask, SQLAlchemy, SQLite | [`CodeAlpha_URLShortener/`](./CodeAlpha_URLShortener) |
| **2** | **Event Registration** | Django, DRF, SQLite | [`CodeAlpha_EventRegistration/`](./CodeAlpha_EventRegistration) |
| **3** | **Restaurant Management** | Django, DRF, SQLite | [`CodeAlpha_RestaurantManagement/`](./CodeAlpha_RestaurantManagement) |
| **4** | **Job Board Platform** | Django, DRF, SQLite | [`CodeAlpha_JobBoard/`](./CodeAlpha_JobBoard) |

---

## 🚀 Task 1: URL Shortener (Flask)
A RESTful API that converts long URLs into short, unique codes.
* **Features:** Cryptographic short code generation, click analytics, and 302 redirects.
* **Security:** Strict `http/https` validation to prevent open-redirects.
* **Architecture:** Factory pattern with thin routing layers and business logic separated into `services.py`.
* **Testing:** Full unit test suite using `pytest`.
👉 **[Read the Task 1 README](./CodeAlpha_URLShortener/README.md)**

---

## 🚀 Task 2: Event Registration System (Django)
A robust API and frontend for managing events and user registrations.
* **Features:** Custom User model (organizers vs. attendees), event capacity management, and registration cancellation logic.
* **Business Logic:** Prevents overbooking and duplicate registrations.
* **Architecture:** Django REST Framework (DRF) with `ViewSets`, custom `@actions` for registration, and a vanilla JS frontend.
👉 **[Read the Task 2 README](./CodeAlpha_EventRegistration/README.md)**

---

## 🚀 Task 3: Restaurant Management System (Django)
A backend API for handling restaurant operations, from inventory to table bookings.
* **Features:** Order processing, table reservations, and automatic inventory deduction when items are ordered.
* **Business Logic:** Implements strict table availability checks (prevents double-booking within a 3-hour window) and capacity validation.
* **Architecture:** Django REST Framework (DRF) with complex relational models (`Order` -> `OrderItem` -> `MenuItem` -> `InventoryItem`).
👉 **[Read the Task 3 README](./CodeAlpha_RestaurantManagement/README.md)**

---

## 🚀 Task 4: Job Board Platform (Django)
A comprehensive API for employers to post jobs and candidates to apply with resumes.
* **Features:** Job listings, advanced search filters (by keyword/location/type), and resume file uploads.
* **Business Logic:** Tracks application statuses, prevents duplicate applications, and restricts visibility based on user roles (Employer vs. Candidate).
* **Architecture:** Django REST Framework (DRF) with `MultiPartParser` for file uploads and custom `@actions` for job applications.
👉 **[Read the Task 4 README](./CodeAlpha_JobBoard/README.md)**

---

## 🛠️ General Setup Instructions
Each project folder contains its own `.venv` and `requirements.txt`. To run any project locally:

1. Navigate into the project directory:
   ```bash
   cd CodeAlpha_ProjectName

2. Set up a virtual environment and install dependencies:

bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
