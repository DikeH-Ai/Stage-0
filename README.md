# Stage 0

## Description

This project is a FastAPI-based web service that provides basic information via a simple API. It includes an email contact, the current UTC timestamp, and a GitHub URL. The project is designed to be lightweight and easy to deploy.

## Setup Instructions

### Prerequisites

Ensure you have the following installed:

- Python 3.9+
- pip (Python package manager)

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/DikeH-Ai/Stage-0
   cd project-name
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   venv\\Scripts\\activate   # On MacOS use ` source venv/bin/activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
5. Access the API at:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## API Documentation

### Root Endpoint

- **URL:** `/`
- **Method:** `GET`
- **Description:** Returns basic project information.

#### **Response Format**

```json
{
  "email": "onyekachi.okomba@gmail.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/DikeH-Ai/Stage-0"
}
```

#### **Example Usage**

```bash
curl -X GET http://127.0.0.1:8000/
```

## Developer Backlink

Looking to hire experienced Python developers? Visit: [https://hng.tech/hire/python-developers](https://hng.tech/hire/python-developers)

---

Feel free to contribute by submitting a pull request or opening an issue!

