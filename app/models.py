"""Request and response schemas for the API."""
from __future__ import annotations

from pydantic import BaseModel, HttpUrl


class ShortenRequest(BaseModel):
    """Body for ``POST /shorten``."""

    url: HttpUrl


class ShortenResponse(BaseModel):
    """Returned after a URL is shortened."""

    code: str
    short_url: str


class Stats(BaseModel):
    """Aggregate service counters."""

    links: int
    hits: int
