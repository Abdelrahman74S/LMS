📚 Library Management System

A full-featured Library Management System built with Django, providing a platform where sellers can list books, manage inventory, and track borrowings, while customers can browse, borrow, and return books easily.

🚀 Features
👤 User Management

Custom user model (MyUser) with extra fields: phone number, address, account type (customer/seller), and optional profile photo (Cloudinary).

Auto-assign users to Customers or Sellers group after registration.

Authentication system:

Register, Login, Logout

Password change & reset

Profile view & update

📚 Books & Categories

Sellers can create, update, delete books and manage categories.

Each book includes:

Title, Author, Description, Category

Price, Copies Available, PDF, and Image (stored in Cloudinary)

Category management: create, update, delete categories.

🔎 Search & Filtering

Advanced search by title, author, or category using django-filters.

📖 Borrowing System

Customers can borrow books if available.

System automatically:

Decreases available copies when a book is borrowed.

Increases available copies when a book is returned.

Tracks due dates and calculates late status.

Sellers can see borrowings for their books.

🔐 Permissions & Security

Borrowing requires login and proper permissions.

Only sellers can manage books and categories (custom UserPassesTestMixin check).

🛠️ Tech Stack
Category	Technology / Service
Backend	Django (Class-Based Views, ORM, Authentication)
Database	SQLite (can easily switch to PostgreSQL/MySQL)
Media Storage	Cloudinary
 for book images & PDFs
Frontend	HTML, CSS, Bootstrap (Django templates)
Filtering	django-filter for search functionality
Auth System	Django's built-in authentication views + custom forms
Deployment Ready	Fully extendable for production (Docker/Cloud deployment supported)
📂 Project Structure
Library-Management/
│
├── account/                # Handles user model, authentication, profiles
│   ├── models.py
│   ├── views.py
│   └── forms.py
│
├── Library/                # Handles books, categories, borrowing logic
│   ├── models.py
│   ├── views.py
│   └── forms.py
│
├── templates/              # All HTML templates for UI
│
├── static/                 # Static assets (CSS, JS)
│
├── manage.py
└── requirements.txt

⚙️ Installation & Setup

Clone the repository

git clone https://github.com/yourusername/library-management.git
cd library-management


Create and activate virtual environment

python -m venv venv
source venv/bin/activate    # Linux / macOS
venv\Scripts\activate       # Windows


Install dependencies

pip install -r requirements.txt


Apply migrations

python manage.py makemigrations
python manage.py migrate


Create a superuser

python manage.py createsuperuser


Run the development server

python manage.py runserver


Open your browser and visit:

http://127.0.0.1:8000/

🌟 Future Enhancements

Add REST API endpoints (Django REST Framework) for mobile/React frontend.

Implement notifications for due dates (email reminders).

Add payment integration for selling books.

Improve UI using modern frontend framework (React, TailwindCSS).
