<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=00E676&height=250&section=header&text=FastAPI%20Task%20Manager&fontSize=65&fontAlignY=38&desc=Secure%20RESTful%20API%20Service&descAlignY=60&descAlign=50" alt="Header Banner">

<h1>⚡ Secure RESTful API Service</h1>

<p>
  <b>A brutally fast, secure, and modern Task Management architecture built on FastAPI.</b>
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3.6+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Framework-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Auth-JWT_Tokens-FF4B4B?style=for-the-badge&logo=jsonwebtokens&logoColor=white" alt="JWT">
  <img src="https://img.shields.io/badge/Database-SQLite3-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
</p>

</div>

---

## 🌌 The Vision

The **FastAPI Task Manager** is a highly-optimized, secure backend service wrapped in a beautifully minimalistic vanilla JavaScript frontend. It is designed to demonstrate stateless authentication, row-level data isolation, and blistering fast API routing without the heavy overhead of modern frontend frameworks.

> **Engineering Note:** This application has been meticulously refactored and pinned to specific dependencies to guarantee backward compatibility with **Python 3.6**, proving that modern API architectures can still run seamlessly on legacy environments.

---

## ⚡ Core Architecture

<table align="center">
  <tr>
    <td align="center" width="50%">
      <img src="https://img.icons8.com/nolan/64/api.png" alt="API"/>
      <h3>High-Performance Routing</h3>
      <p>Powered by FastAPI and Starlette, delivering NodeJS-level speed with automatic Swagger UI documentation.</p>
    </td>
    <td align="center" width="50%">
      <img src="https://img.icons8.com/nolan/64/security-checked.png" alt="Security"/>
      <h3>Stateless Security</h3>
      <p>Implements robust OAuth2 Password Bearer flows with Bcrypt hashed passwords and JWT token validation.</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://img.icons8.com/nolan/64/database.png" alt="Data"/>
      <h3>Row-Level Isolation</h3>
      <p>Strict SQLAlchemy ORM filtering ensures users have zero-knowledge access to anything outside their own tasks.</p>
    </td>
    <td align="center">
      <img src="https://img.icons8.com/nolan/64/laptop.png" alt="UI"/>
      <h3>Minimal SaaS Aesthetic</h3>
      <p>A server-side rendered Jinja2 interface featuring a dynamic Dark/Light mode toggle powered by native CSS variables.</p>
    </td>
  </tr>
</table>

---

## 🔐 Authentication Flow

<div align="center">

```mermaid
sequenceDiagram
    participant User
    participant Frontend
    participant FastAPI
    participant Database

    User->>Frontend: Enters Credentials
    Frontend->>FastAPI: POST /token (OAuth2 Form)
    FastAPI->>Database: Fetch User & Verify Bcrypt Hash
    Database-->>FastAPI: Hash Matches
    FastAPI-->>Frontend: Return JWT Access Token
    Frontend->>Frontend: Store Token in LocalStorage
    User->>Frontend: Create New Task
    Frontend->>FastAPI: POST /tasks (Headers: Bearer <Token>)
    FastAPI->>FastAPI: Decode JWT & Authorize
    FastAPI->>Database: Save Task mapped to User ID
    Database-->>FastAPI: Success
    FastAPI-->>Frontend: HTTP 201 Created
```

</div>

---

## 🚀 Ignition Sequence (Setup Guide)

<details>
<summary><b>Click here to view installation & deployment instructions</b></summary>
<br>

### 1. Clone the Repository
```bash
git clone https://github.com/TarakShetti/FastAPI-task-manager.git
cd FastAPI-task-manager
```

### 2. Initialize Virtual Environment
```bash
python -m venv venv

# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Launch the Server
Start the FastAPI server using Uvicorn:
```bash
uvicorn main:app --reload
```

</details>

---

## 💻 Interactive Dashboards

Once the server is running, navigate to the following endpoints:

* 🌐 **Application UI:** [http://127.0.0.1:8000](http://127.0.0.1:8000)
* 📖 **Swagger API Docs:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* 📘 **ReDoc API Docs:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

<div align="center">
  <p><i>Fast APIs. Secure Tokens. Elegant UIs.</i></p>
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00E676&height=100&section=footer" width="100%" alt="Footer Banner">
</div>
