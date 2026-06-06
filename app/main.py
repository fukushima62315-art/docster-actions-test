"""quicklink HTTP API.

A minimal URL shortener built with FastAPI:

* ``POST /shorten`` registers a URL and returns a short code.
* ``GET /{code}`` redirects to the original URL.
* ``GET /api/stats`` reports how many links and hits have been served.

Run locally with::

    uvicorn app.main:app --reload
"""
from __future__ import annotations

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse

from . import store
from .models import ShortenRequest, ShortenResponse, Stats

app = FastAPI(title="quicklink", version="0.1.0")


@app.post("/shorten", response_model=ShortenResponse)
def shorten(body: ShortenRequest, request: Request) -> ShortenResponse:
    """Create a short code for the given URL."""
    code = store.add(str(body.url))
    short_url = str(request.base_url).rstrip("/") + "/" + code
    return ShortenResponse(code=code, short_url=short_url)


@app.get("/api/stats", response_model=Stats)
def get_stats() -> Stats:
    """Return aggregate link and hit counters."""
    return Stats(**store.stats())


@app.get("/{code}")
def follow(code: str) -> RedirectResponse:
    """Redirect to the URL behind ``code`` (404 if unknown)."""
    url = store.resolve(code)
    if url is None:
        raise HTTPException(status_code=404, detail="unknown short code")
    return RedirectResponse(url)
