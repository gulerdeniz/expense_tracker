# Expense Tracker API

## Version

  v1.2.0
- cleaner architecture
- separation of concerns
- easier testing
- more scalable structure

A Python-based backend API that allows users to create, read, update, and delete expenses. Built using FastAPI and SQLAlchemy ORM.

---

## Features

* Full CRUD operations:

  * Create expense
  * Read all expenses
  * Read single expense by ID
  * Update expense
  * Delete expense
* SQLite database integration
* ORM support with SQLAlchemy
* Request validation with Pydantic
* Automatic API documentation (Swagger UI)

---

## Tech Stack

* Python
* FastAPI
* SQLAlchemy (ORM)
* SQLite
* Pydantic
* Uvicorn

---

## Project Structure

```
expense_tracker/
│
├── main.py          # API endpoints
├── database.py      # DB connection & session
├── models.py        # ORM models
├── schemas.py       # Request/Response schemas
├── requirements.txt
└── README.md
```

---

## API Endpoints

### Create Expense

```
POST /expenses
```

### Get All Expenses

```
GET /expenses
```

### Get Expense by ID

```
GET /expenses/{id}
```

### Update Expense

```
PUT /expenses/{id}
```

### Delete Expense

```
DELETE /expenses/{id}
```

---

## Example Request (POST)

```json
{
  "amount": 100,
  "category": "food",
  "description": "dinner",
  "date": "2026-03-17"
}
```

---

## Running the Project

### 1. Create virtual environment

```
python -m venv venv
```

### 2. Activate environment

Windows:

```
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run server

```
uvicorn main:app --reload
```

---

## API Documentation

Once the server is running, open:

```
http://127.0.0.1:8000/docs
```

Interactive Swagger UI will allow you to test all endpoints.

---

## Future Improvements

* Add authentication (JWT)
* Add category-based reports
* Refactor into service/crud layer
* Add unit and integration tests
* Support PostgreSQL

---

## Purpose

This project is built as part of learning backend development with Python, focusing on API design, ORM usage, and clean architecture.

---
