# FastAPI Task Manager API

A robust, RESTful API built with **FastAPI** and **SQLAlchemy**. This project demonstrates a complete backend architecture featuring stateless JWT authentication, password hashing, and role-based access control (RBAC) where users can only manage their own data.

## 🚀 Tech Stack

* **Framework:** FastAPI (High-performance Python web framework)
* **Database:** SQLite (SQLAlchemy ORM)
* **Authentication:** JWT (JSON Web Tokens) & OAuth2
* **Security:** Passlib (Bcrypt password hashing)
* **Validation:** Pydantic Schemas

## ✨ Features

* **User Authentication:** Secure Signup/Login with hashed passwords.
* **Stateless Sessions:** JWT-based authentication flow.
* **CRUD Operations:** Create, Read, Update, and Delete tasks.
* **Authorization:** Row-level security (users cannot access tasks they don't own).
* **Auto-Documentation:** Interactive Swagger UI integration.

## 🛠️ Installation & Setup

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/yourusername/task-manager.git](https://github.com/yourusername/task-manager.git)
    cd task-manager
    ```

2.  **Create a Virtual Environment**
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Server**
    ```bash
    uvicorn app.main:app --reload
    ```

## 📚 API Documentation

Once the server is running, you can explore the interactive API docs at:

* **Swagger UI:** `http://127.0.0.1:8000/docs`
* **ReDoc:** `http://127.0.0.1:8000/redoc`

## 📂 Project Structure