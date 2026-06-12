# 📝 Task Manager REST API

A production-ready REST API built with **FastAPI**, **SQLite**, and **JWT Authentication**.  
Full CRUD operations, user authentication, and auto-generated API docs included.

---

## 🚀 Features

- ✅ User Registration & Login with JWT tokens
- ✅ Create, Read, Update, Delete tasks
- ✅ Filter tasks by priority (low / medium / high) or status (completed / pending)
- ✅ Each user only sees their own tasks (secure)
- ✅ Auto-generated interactive API docs (Swagger UI)
- ✅ Clean folder structure — easy to extend

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| Database | SQLite + SQLAlchemy ORM |
| Auth | JWT (JSON Web Tokens) |
| Validation | Pydantic v2 |
| Password Hashing | bcrypt |
| Server | Uvicorn |

---

## 📁 Project Structure

```
task-manager-api/
├── main.py               # App entry point
├── database.py           # DB connection & session
├── requirements.txt      # Dependencies
├── models/
│   └── models.py         # SQLAlchemy models (User, Task)
├── schemas/
│   └── schemas.py        # Pydantic schemas
├── routers/
│   ├── auth.py           # /auth/register, /auth/login
│   └── tasks.py          # Full CRUD for tasks
└── core/
    └── security.py       # JWT creation & password hashing
```

---

## ⚡ Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/Peter-Akacha/task-manager-api.git
cd task-manager-api
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the server
```bash
uvicorn main:app --reload
```

### 4. Open API docs
```
http://127.0.0.1:8000/docs
```

---

## 🔐 API Endpoints

### Authentication
| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/register` | Create new account |
| POST | `/auth/login` | Login & get JWT token |

### Tasks (requires JWT token)
| Method | Endpoint | Description |
|---|---|---|
| GET | `/tasks/` | Get all your tasks |
| POST | `/tasks/` | Create a new task |
| GET | `/tasks/{id}` | Get a single task |
| PUT | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |

---

## 🧪 Example Usage

**Register:**
```json
POST /auth/register
{
  "username": "peter",
  "email": "peter@example.com",
  "password": "securepassword"
}
```

**Create a Task:**
```json
POST /tasks/
Authorization: Bearer <your_token>
{
  "title": "Build portfolio project",
  "description": "FastAPI + SQLite REST API",
  "priority": "high"
}
```

---

## 🌐 Deployment

Deploy free on **[Render.com](https://render.com)**:
1. Push this repo to GitHub
2. Create a new Web Service on Render
3. Set start command: `uvicorn main:app --host 0.0.0.0 --port 10000`
4. Done — live URL in minutes!

---

## 👨‍💻 Author

**Peter Akacha** — Python & Web Developer  
Available for freelance projects on [Upwork](https://upwork.com)

---

## 📄 License

MIT License — free to use and modify.
