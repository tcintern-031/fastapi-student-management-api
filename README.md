# FastAPI Student Management API

A beginner-friendly REST API built with **FastAPI** as part of my AI Engineering internship.

## 🚀 Features

* Get all students
* Get a student by ID
* Add a new student
* Update a student
* Delete a student
* Pydantic request validation
* HTTP 404 error handling
* Interactive Swagger API documentation

## 🛠️ Technologies

* Python
* FastAPI
* Pydantic
* Uvicorn

## 📁 Project Structure

```text
Day 03 FastAPI Student Management API/
│
├── main.py
├── model.py
├── requirements.txt
└── README.md
```

## ▶️ How to Run

### 1. Create virtual environment

```bash
python -m venv myenv
```

### 2. Activate virtual environment

Windows PowerShell:

```powershell
.\myenv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
uvicorn main:app --reload
```

## 📖 API Documentation

After starting the server, open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI can be used to test all API endpoints interactively.

## 🔗 API Endpoints

| Method | Endpoint         | Description       |
| ------ | ---------------- | ----------------- |
| GET    | `/`              | Basic greeting    |
| GET    | `/students`      | Get all students  |
| GET    | `/students/{id}` | Get student by ID |
| POST   | `/students`      | Add a new student |
| PUT    | `/students/{id}` | Update a student  |
| DELETE | `/students/{id}` | Delete a student  |

## 🧠 Concepts Learned

* FastAPI application setup
* API routes and HTTP methods
* Path parameters
* Request body
* Pydantic `BaseModel`
* Automatic data validation
* HTTP exceptions and status codes
* CRUD operations
* Python lists and dictionaries in API development
* `enumerate()` for accessing list indexes
* Swagger/OpenAPI documentation

## ⚠️ Note

This project currently uses an in-memory Python list as the data source instead of a database. Therefore, changes made during runtime are lost when the server restarts.

## 🎯 Internship Task

**Day 03 — FastAPI Fundamentals & Student Management API**

Built as part of my AI Engineering internship to understand how Python APIs are created and tested using FastAPI.
