"""A minimal URL shortener backed by an in-memory dict (demo for Docster)."""
from __future__ import annotations

import secrets
import string

_STORE: dict[str, str] = {}
_ALPHABET = string.ascii_letters + string.digits


def shorten(url: str, length: int = 6) -> str:
    """Create a short code for a URL and return the code."""
    code = "".join(secrets.choice(_ALPHABET) for _ in range(length))
    _STORE[code] = url
    return code


def resolve(code: str) -> str | None:
    """Return the original URL for a short code, or None if unknown."""
    return _STORE.get(code)


def count() -> int:
    """Return how many URLs have been shortened so far."""
    return len(_STORE)
