# Secure RESTful API Service (Modernized)

This repository contains a robust, secure, and modern Task Management application. It consists of a high-performance **FastAPI** backend and a beautifully designed, responsive vanilla frontend.

## 🚀 Features & Architecture

* **Backend Framework:** FastAPI with automatic Swagger UI (`/docs`).
* **Database:** SQLite with SQLAlchemy ORM.
* **Authentication:** Stateless JSON Web Tokens (JWT) & OAuth2 Password Bearer flow.
* **Security:** Bcrypt password hashing (Passlib) and Row-Level Security (users only see their tasks).
* **Frontend UI:** 
  * Server-side rendered Jinja2 templates.
  * Modern, switchable Dark/Light Mode using CSS Variables.
  * Clean, minimal SaaS aesthetic inspired by Notion and Linear.
  * Fully responsive CSS Grid and Flexbox layouts.
  * Interactive vanilla JavaScript for dynamic API requests without page reloads.

## 🐍 Python 3.6+ Compatibility

This application has been meticulously refactored and pinned to specific dependencies to guarantee backward compatibility with **Python 3.6**. 

**Compatibility Fixes Included:**
* Removed all Python 3.7+ typing features (e.g., uses `typing.List` instead of `list[]`).
* Removed `from __future__ import annotations`.
* Downgraded FastAPI (`0.68.2`) and Pydantic (`1.8.2`) to their last known stable versions supporting Python 3.6.
* Removed reliance on newer `asyncio` APIs, `dataclasses`, and `match/case` syntax.

---

## 🛠️ Installation & Setup (Beginner Friendly)

Follow these exact steps to run the application on your machine.

### 1. Clone the Repository
```bash
git clone https://github.com/TarakShetti/Secure-RESTful-API-Service-with-Stateless-Authentication-Data-Isolation
cd Secure-RESTful-API-Service-with-Stateless-Authentication-Data-Isolation
```

### 2. Create a Virtual Environment
It is best practice to use a virtual environment so dependencies don't conflict.

```bash
python -m venv venv
```

**Activate the Environment:**
* **Windows:**
  ```bash
  venv\Scripts\activate
  ```
* **Linux/macOS:**
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies
Ensure your virtual environment is active (you should see `(venv)` in your terminal prompt), then run:

```bash
pip install -r requirements.txt
```

### 4. Run the Application
Start the FastAPI server using Uvicorn:

```bash
uvicorn main:app --reload
```

---

## 💻 Usage

Once the server is running, open your web browser and navigate to:
**http://127.0.0.1:8000**

1. **Sign Up:** Click "Sign up" to create a new account.
2. **Dashboard:** You will be automatically redirected to the Task Dashboard.
3. **Toggle Theme:** Click the moon/sun icon in the top left to switch between Dark and Light mode.
4. **Manage Tasks:** Create new tasks, check them off, edit, or delete them.

### API Documentation
For developers wanting to interact directly with the API endpoints, visit:
* Swagger UI: **http://127.0.0.1:8000/docs**
* ReDoc: **http://127.0.0.1:8000/redoc**

---

## 🔧 Troubleshooting

* **ModuleNotFoundError: No module named 'fastapi'**: Ensure you activated your virtual environment before running `pip install` and starting the server.
* **SyntaxError**: Ensure you are running at least Python 3.6. If you are using Python 3.5 or below, FastAPI will not compile.

## 🔮 Future Enhancements
* **Task Prioritization:** Add High/Medium/Low priority flags to the `Task` model.
* **Drag-and-Drop:** Implement a Kanban board layout for tasks.
* **Email Verification:** Send an activation email when a user registers before allowing login.
