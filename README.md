# NeoSapX Backend

Backend MVP for a retail operations system (restocking + expiry tracking).  
Built with **FastAPI**.

---

## Setup (Windows)

### 1. Create Virtual Environment
```powershell
python -m venv venv
```

### 2. Activate Virtual Environment
```powershell
.\venv\Scripts\Activate
```

### 3. Install Dependencies
```powershell
pip install -r requirements.txt
```

---

## Run the API Server

```powershell
uvicorn app.main:app --reload
```

---

## Access the API

API Root  
```
http://127.0.0.1:8000/
```

Interactive API Documentation (Swagger UI)  
```
http://127.0.0.1:8000/docs
```

---

## Project Structure

```
neosapX
│
├── app
│   ├── main.py        # FastAPI entry point
│   ├── api            # API routes (to be added)
│   ├── models         # Database models (to be added)
│   ├── schemas        # Request/response validation
│   ├── services       # Business logic layer
│   └── core           # Configuration / security
│
├── venv               # Python virtual environment
├── requirements.txt   # Project dependencies
└── README.md
```

---

## Notes

This project is the backend MVP for a retail automation system designed to:

- Track product restocking
- Manage expiry batches
- Generate operational alerts
- Support automation workflows for small grocery stores