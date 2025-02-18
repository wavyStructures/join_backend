# Task Management API

This project is a Django-based API for managing tasks, users, and contacts. It is designed to support features such as user authentication, task assignment, and contact management.

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Models](#models)
- [Authentication](#authentication)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or higher
- Django 5.1.4 or higher
- Django Rest Framework
- Postman (optional, for API testing)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/wavyStructures/join_backend
   cd your-repo-name
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**

   - Run the migrations to create the necessary database tables:
     ```bash
     python manage.py migrate
     ```

5. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

## Running the Application

After starting the development server, the API will be available at `http://127.0.0.1:8000`. You can test the endpoints using Postman or any other API client.

## API Endpoints

### User Authentication

- **Login:**
  - `POST /api/login/`
  - Request Body:
    ```json
    {
      "email": "user@example.com",
      "password": "password"
    }
    ```
  - Response:
    ```json
    {
      "user": {
        "id": 34,
        "username": "user",
        "email": "user@example.com"
      },
      "token": "73450b0037b5e6cf3dad626f1be8517078e0efce"
    }
    ```

### User Management

- **Create User:**

  - `POST /auth/users/`
  - Request Body:
    ```json
    {
      "username": "user",
      "email": "user@example.com",
      "password": "password"
    }
    ```
  - Response:

    ```json
    {
      "id": 34,
      "password": "pbkdf2_sha256$870000$fOJQ5s4l5eM913ZIt3CBlj$M6wyxD1i99M+kLCdY0jhoEsyaL/ari3W7eSmt9gax2Q=",
      "last_login": null,
      "is_superuser": false,
      "first_name": "",
      "last_name": "",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2025-02-18T12:35:22.066312Z",
      "username": "user",
      "email": "user@example.com",
      "phone": "123456789",
      "contactColor": "#a64dff",
      "is_guest": false,
      "groups": [],
      "user_permissions": []
    }
    ```

- **Get All Users:**
  - `GET /auth/users/`
  - Response: List of all users.

### Task Management

- **Get All Tasks:**

  - `GET /tasks/`
  - Response: List of all tasks.

- **Get Task by ID:**

  - `GET /tasks/<id>/`
  - Response: Task details.

- **Create Task:**

  - `POST /api/tasks/`
  - Request Body:
    ```json
    {
      "owner": "anja_schwab@gmx.de",
      "assigned_to": [],
      "title": "New Task",
      "category": "Work",
      "description": "more details",
      "status": "todo",
      "created_at": "2025-01-29T09:00:08.841839Z",
      "updated_at": "2025-02-17T09:14:04.697132Z",
      "category": "category-2",
      "due_date": "2024-06-14",
      "priority": "medium",
      "task_type": "technical_task"
    }
    ```

- **Update Task:**

  - `PUT /tasks/<id>/`
  - Request Body: Same as for task creation.

- **Delete Task:**
  - `DELETE /tasks/<id>/`

### Contact Management

- **Get All Contacts:**

  - `GET /contacts/`
  - Response: List of all contacts.

- **Create Contact:**

  - `POST /contacts/`
  - Request Body:
    ```json
    {
      "username": "John Doe",
      "phone": "123456789",
      "email": "john.doe@example.com",
      "contactColor": "#76b852",
      "contact_is_a_user": true,
      "is_public": false,
      "user": 1
    }
    ```

- **Update Contact:**

  - `PUT /contacts/<id>/`
  - Request Body: Same as for contact creation.

- **Delete Contact:**
  - `DELETE /contacts/<id>/`

## Models

- **TaskItem**: Represents a task with fields like title, description, status, category, due date, priority, and type. It also includes relationships to users (owner) and contacts (assigned_to). Tasks can have different statuses, priorities, and categories, as well as a type that classifies them (e.g., technical task, management task, etc.).
- **Subtask**: Represents a subtask linked to a `TaskItem`.
- **CustomUser**: Extends Django's AbstractUser with additional fields like contactColor, phone, and is_guest. It uses email as the unique identifier (USERNAME_FIELD = 'email') and a custom user manager (CustomUserManager). The contactColor is automatically assigned a random value unless the user is a guest. The model also supports spaces in usernames and sets an unusable password for guest users.
- **Contacts**: Stores information about contacts. They are all available to all users. Every user is also a contact.

## Authentication

This project uses token-based authentication. To access protected endpoints, include the token in the `Authorization` header as follows:

```
'Authorization': `Token ${token}`
```

## Contributing

Contributions are welcome! Please create an issue first to discuss what you would like to change. You can also fork the repository, make changes, and submit a pull request.
