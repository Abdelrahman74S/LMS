# Library Management System (LMS)

A web application built with Django for managing a library's collection of books. Users can browse, search, and borrow books. Sellers/Librarians can manage the book inventory.

## Features

*   **User Authentication**: Secure login and registration for users.
*   **Two User Roles**:
    *   **Borrowers**: Can browse, search, and borrow books.
    *   **Sellers/Librarians**: Can manage the book inventory.
*   **Book Management**:
    *   Sellers can add new books with details like title, author, description, category, price, available copies, an image, and a PDF file.
    *   Sellers can update and delete their own book listings.
    *   A comprehensive list of all books is available to all users.
*   **Category Management**: Sellers can create and manage book categories.
*   **Search and Filter**: Users can easily search for books.
*   **Borrowing System**:
    *   Authenticated users can borrow available books.
    *   The number of available copies is tracked.
    *   Users can view a list of their currently borrowed books.
    *   Users can view the PDF of a book once they have borrowed it.

## Technologies Used

*   **Backend**: Python, Django
*   **Frontend**: HTML, CSS, Bootstrap
*   **Forms**: `django-crispy-forms`
*   **Database**: SQLite (default)

## Setup and Installation

To get a local copy up and running, follow these simple steps.

### Prerequisites

*   Python 3.8+
*   pip

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/Abdelrahman74S/LMS.git

    ```

2.  **Create and activate a virtual environment:**
    ```sh
    python -m venv env
    # On Windows
    env\Scripts\activate
    # On macOS/Linux
    source env/bin/activate
    ```

3.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    ```sh
    python manage.py migrate
    ```

5.  **Run the development server:**
    ```sh
    python manage.py runserver
    ```

The application will be available at `http://127.0.0.1:8000/`.
