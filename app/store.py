"""In-memory storage for short codes.

This is a process-local store: codes live only as long as the server runs.
Swap this module for a Redis- or Postgres-backed implementation to persist
links across restarts.
"""
from __future__ import annotations

import secrets
import string

_ALPHABET = string.ascii_letters + string.digits
_CODE_LENGTH = 6

# code -> original URL
_links: dict[str, str] = {}
# code -> number of times it was resolved
_hits: dict[str, int] = {}


def _new_code() -> str:
    """Generate a random short code that is not already in use."""
    while True:
        code = "".join(secrets.choice(_ALPHABET) for _ in range(_CODE_LENGTH))
        if code not in _links:
            return code


def add(url: str) -> str:
    """Store a URL and return its freshly minted short code."""
    code = _new_code()
    _links[code] = url
    _hits[code] = 0
    return code


def resolve(code: str) -> str | None:
    """Return the original URL for a code, counting the hit.

    Returns ``None`` when the code is unknown.
    """
    url = _links.get(code)
    if url is not None:
        _hits[code] += 1
    return url


def stats() -> dict[str, int]:
    """Return aggregate counters for the service."""
    return {"links": len(_links), "hits": sum(_hits.values())}
