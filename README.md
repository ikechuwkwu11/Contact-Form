# 📬 Contact Form API with User Authentication (Flask)

This is a simple Flask-based backend API for a **Contact Form** system that includes **user registration, login/logout**, and full CRUD operations for contact messages. It uses **SQLite** for the database and **Flask-Login** for user session management.

---

## 🚀 Features

- ✅ User registration with password hashing
- ✅ User login & logout with session handling
- ✅ Submit contact messages
- ✅ View all submitted messages
- ✅ View a single message
- ✅ Edit a message
- ✅ Delete a message

---

## 🛠️ Technologies Used

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Login
- SQLite
- Werkzeug (for password hashing)

---

## 📂 Project Structure

📁 your_project/
│
├── app.py # Main application with all routes
├── models.py # SQLAlchemy models
├── contact_message.db # SQLite database (auto-generated)
├── README.md # This file
└── requirements.txt # (Optional) List of dependencies


---

## 🔐 Authentication Routes

### Register a User
**POST** `/register`

**Request JSON:**
```json
{
  "username": "john_doe",
  "password": "securepassword"
}

Login
POST /login

Request JSON:
{
  "username": "john_doe",
  "password": "securepassword"
}


Logout
GET /logout

📨 Contact Message Routes
Add a Message
POST /contact_message

Request JSON:
{
  "name": "Jane Doe",
  "email": "jane@example.com",
  "subject": "Feedback",
  "message": "I love your app!"
}

Get All Messages
GET /get_contact_message

Get a Single Message
GET /single_contact_message/<id>

Edit a Message
PUT /edit_contact_message/<id>

Request JSON:
{
  "name": "Jane Updated",
  "email": "new@example.com",
  "subject": "New Subject",
  "message": "Updated message text"
}

Delete a Message
DELETE /delete_contact_message/<id>

🔒 Note
Make sure to replace the SECRET_KEY in app.config with a strong secret in production.
Flask
Flask-Login
Flask-SQLAlchemy
Werkzeug
