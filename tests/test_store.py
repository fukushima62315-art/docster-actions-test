"""Unit tests for the in-memory store."""
from app import store


def test_shorten_then_resolve_roundtrip():
    code = store.add("https://example.com/page")
    assert store.resolve(code) == "https://example.com/page"


def test_resolve_unknown_code_returns_none():
    assert store.resolve("nope-xyz") is None


def test_stats_counts_links_and_hits():
    before = store.stats()["links"]
    code = store.add("https://example.org")
    store.resolve(code)
    store.resolve(code)
    after = store.stats()
    assert after["links"] == before + 1
    assert after["hits"] >= 2
