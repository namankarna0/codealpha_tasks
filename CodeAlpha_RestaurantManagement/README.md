# Task 3: Restaurant Management System (Django)

A full-stack backend API for handling restaurant operations, including menu management, table reservations, order processing, and inventory tracking.

## 🚀 Features
- **Inventory Management:** Track stock for ingredients (e.g., Beef Patty).
- **Menu Management:** Create menu items with prices.
- **Order Processing:** Create orders and add items to them.
- **Inventory Auto-Update:** When a menu item is ordered, the backend automatically deducts the required ingredients from the inventory. (e.g., Ordering a Burger drops the Beef Patty stock).
- **Table Reservations:** Book tables with strict validation.
- **Table Availability Check:** Automatically blocks double-booking by checking for overlapping 3-hour reservation windows.
- **Capacity Validation:** Prevents booking a table if the number of guests exceeds the table's capacity.

## 🛠️ Tech Stack
- **Framework:** Django & Django REST Framework (DRF)
- **Database:** SQLite
- **Authentication:** Basic Auth (for API testing)

## ⚙️ Local Setup Instructions

1. **Navigate to this folder:**
   ```bash
   cd CodeAlpha_RestaurantManagement

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
(Requires Basic Auth: admin / your_password)

Method	Endpoint	Description
GET/POST	/api/menu/	List or create menu items
GET/POST	/api/inventory/	List or create inventory stock
GET/POST	/api/tables/	List or create tables
GET/POST	/api/reservations/	List or create reservations
GET/POST	/api/orders/	List or create orders
POST	/api/orders/<id>/add_item/	Add a menu item to an order (auto-deducts inventory)
text

