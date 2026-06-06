# quicklink

A minimal URL shortener API built with FastAPI that registers short codes for URLs and tracks redirect hits.

## Key features

- **POST /shorten** – Register a URL and receive a unique short code
- **GET /{code}** – Redirect to the original URL (404 if code is unknown)
- **GET /api/stats** – View aggregate link and hit counters
- In-memory storage (process-local; swap `store.py` for persistent backends like Redis or Postgres)

## Technology stack

- **Language**: Python
- **Framework**: FastAPI
- **Server**: Uvicorn
- **Validation**: Pydantic
- **Testing**: pytest, httpx

## Installation / setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd docster-actions-test
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the server:
   ```bash
   uvicorn app.main:app --reload
   ```

   The API will be available at `http://localhost:8000`.

## Usage

**Shorten a URL:**
```bash
curl -X POST http://localhost:8000/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com/very/long/path"}'
```

**Follow a short code:**
```bash
curl -L http://localhost:8000/abc123
```

**View statistics:**
```bash
curl http://localhost:8000/api/stats
```

**Run tests:**
```bash
pytest
```

## Directory structure

```
.
├── app/
│   ├── __init__.py          # Package metadata
│   ├── main.py              # FastAPI application and endpoint handlers
│   ├── models.py            # Pydantic request/response schemas
│   └── store.py             # In-memory storage implementation
├── tests/
│   └── test_store.py        # Unit tests for the store module
└── requirements.txt         # Python dependencies
```