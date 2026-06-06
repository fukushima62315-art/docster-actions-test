# Docster Actions Test 2

A minimal URL shortener backed by an in-memory dictionary, designed as a demo for Docster.

## Key features

- Create short codes for URLs with configurable length
- Resolve short codes back to original URLs
- Track the count of shortened URLs
- In-memory storage (no persistence)

## Technology stack

- **Language:** Python
- **Libraries:** `secrets`, `string` (standard library)

## Installation / setup

Clone the repository and ensure Python is available:

```bash
git clone https://github.com/fukushima62315-art/docster-actions-test2.git
cd docster-actions-test2
```

No external dependencies required; uses only Python standard library.

## Usage

Import and use the module functions:

```python
from app import shorten, resolve, count

# Create a short code for a URL
code = shorten("https://example.com/very/long/url")
print(code)  # e.g., "aB3xYz"

# Resolve a short code back to the original URL
original = resolve(code)
print(original)  # https://example.com/very/long/url

# Check how many URLs have been shortened
print(count())  # 1
```

Customize the short code length:

```python
code = shorten("https://example.com", length=10)
```

## Directory structure

```
.
├── app.py              # Main module with shorten, resolve, and count functions
└── README.md
```
