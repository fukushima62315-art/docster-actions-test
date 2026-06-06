# quicklink

A minimal URL shortener HTTP API built with FastAPI.

## Key features

- **POST /shorten** — Register a URL and receive a short code
- **GET /{code}** — Redirect to the original URL behind a short code
- **GET /api/stats** — View aggregate link and hit counters
- In-memory storage (process-local; designed for swapping in persistent backends like Redis or PostgreSQL)

## Technology stack

- **Language:** Python
- **Framework:** FastAPI
- **Server:** Uvicorn
- **Validation:** Pydantic
- **Testing:** pytest, httpx

## Installation / setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Start the development server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

**Create a short link:**
```bash
curl -X POST http://localhost:8000/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com/very/long/path"}'
```

**Follow a short link:**
```bash
curl -L http://localhost:8000/abc123
```

**View statistics:**
```bash
curl http://localhost:8000/api/stats
```

Run tests:
```bash
pytest
```

## Directory structure

```
app/
  __init__.py          — Package metadata
  main.py              — FastAPI application and route handlers
  models.py            — Pydantic request/response schemas
  store.py             — In-memory URL and hit storage
tests/
  test_store.py        — Unit tests for the store module
requirements.txt       — Project dependencies
```