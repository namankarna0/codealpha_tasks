# CodeAlpha Backend Development Internship Tasks

Welcome to my repository for the CodeAlpha Backend Development Internship. This repository contains full-stack backend projects built from scratch, demonstrating RESTful API design, database modeling, and secure authentication.

## 📂 Projects Overview

| Task | Project | Tech Stack | Directory |
| :--- | :--- | :--- | :--- |
| **1** | **URL Shortener** | Flask, SQLAlchemy, SQLite | [`CodeAlpha_URLShortener/`](./CodeAlpha_URLShortener) |
| **2** | **Event Registration** | Django, DRF, SQLite | [`CodeAlpha_EventRegistration/`](./CodeAlpha_EventRegistration) |
| **3** | Restaurant Management | Django, DRF | *Coming Soon* |
| **4** | Job Board Platform | Django, DRF | *Coming Soon* |

---

## 🚀 Task 1: URL Shortener (Flask)
A RESTful API that converts long URLs into short, unique codes.
* **Features:** Generates cryptographic short codes, handles collisions safely via database constraints, tracks click analytics, and uses 302 redirects.
* **Security:** Strict `http/https` validation to prevent open-redirects and XSS attacks.
* **Architecture:** Factory pattern with thin routing layers and business logic separated into `services.py`.
👉 **[Read the Task 1 README](./CodeAlpha_URLShortener/README.md)**

---

## 🚀 Task 2: Event Registration System (Django)
A robust API and frontend for managing events and user registrations.
* **Features:** Custom User model (organizers vs. attendees), event capacity management, and registration cancellation logic.
* **Security:** Token/Session-based authentication and custom permission classes.
* **Architecture:** Django REST Framework (DRF) with `ViewSets`, custom `@actions` for registration, and a vanilla JS frontend.
👉 **[Read the Task 2 README](./CodeAlpha_EventRegistration/README.md)**

---

## 🛠️ General Setup Instructions
Each project folder contains its own `.venv` and `requirements.txt`. To run any project locally:

1. Navigate into the project directory:
   ```bash
   cd CodeAlpha_ProjectName