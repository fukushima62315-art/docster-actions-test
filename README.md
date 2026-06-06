# quicklink

A minimal URL shortener built with FastAPI that registers URLs and provides short redirecting codes.

## Key features

- **POST /shorten** — register a URL and receive a short code
- **GET /{code}** — redirect to the original URL (returns 404 if unknown)
- **GET /api/stats** — view aggregate link and hit counters
- In-memory storage (process-local; suitable for single-instance deployments)

## Technology stack

- **Language:** Python
- **Framework:** FastAPI
- **Server:** Uvicorn
- **Validation:** Pydantic

## Installation / setup

1. Clone the repository and navigate to the project root.
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

**Example requests:**

```bash
# Shorten a URL
curl -X POST http://localhost:8000/shorten \
  -H "Content-Type: application/json" \
  -d '{"url":"https://example.com/long/path"}'

# Follow a short code
curl -L http://localhost:8000/ABC123

# View statistics
curl http://localhost:8000/api/stats
```

## Directory structure

```
.
├── app/
│   ├── __init__.py          # Package metadata
│   ├── main.py              # FastAPI application and endpoints
│   ├── models.py            # Request/response schemas
│   └── store.py             # In-memory link storage
├── tests/
│   └── test_store.py        # Unit tests for the store module
└── requirements.txt         # Python dependencies
```