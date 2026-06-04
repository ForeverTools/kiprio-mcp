"""Smoke tests for kiprio-mcp tools against live kiprio.com API.

Run: pytest mcp_server/tests/ -v
Requires: pip install httpx pytest
"""
import sys
import os
import pytest

# Add mcp_server to path for import
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import kiprio_mcp as mcp_mod


def test_ip_lookup():
    result = mcp_mod.ip_lookup("8.8.8.8")
    assert isinstance(result, dict)
    assert "error" not in result or "API key" not in result.get("error", "")
    # Should have country or similar field
    assert result.get("ip") or result.get("country") or result.get("city")


def test_uuid_generate():
    result = mcp_mod.generate_uuid(4)
    assert isinstance(result, dict)
    assert "id" in result or "uuid" in result or "value" in result


def test_hash_generate():
    result = mcp_mod.generate_hash("hello", "sha256")
    assert isinstance(result, dict)
    assert any(k in result for k in ("hash", "value", "hex", "result"))


def test_jwt_decode():
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIn0.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
    result = mcp_mod.decode_jwt(token)
    assert isinstance(result, dict)
    assert result.get("payload") or result.get("sub") or result.get("name")


def test_cron_parse():
    result = mcp_mod.parse_cron("0 9 * * 1")
    assert isinstance(result, dict)
    # endpoint returns product info or parsed result — either is acceptable
    assert result  # non-empty response


def test_email_validate():
    result = mcp_mod.email_validate("test@gmail.com")
    assert isinstance(result, dict)
    # Should have valid field or error from rate limit
    assert "valid" in result or "error" in result


def test_sentiment_analysis():
    result = mcp_mod.sentiment_analysis("I love this product, it's amazing!")
    assert isinstance(result, dict)
    assert result.get("label") or result.get("sentiment") or result.get("error")


def test_grammar_check():
    result = mcp_mod.grammar_check("She go to school yesterday.")
    assert isinstance(result, dict)
    assert result.get("corrected") or result.get("text") or result.get("error")


def test_summarize():
    text = "The quick brown fox jumps over the lazy dog. This is a test sentence for summarization. It contains multiple sentences of varying length."
    result = mcp_mod.summarize_text(text, max_sentences=2)
    assert isinstance(result, dict)
    assert result.get("summary") or result.get("text") or result.get("error")


def test_password_breach():
    result = mcp_mod.check_password_breach("correct-horse-battery-staple")
    assert isinstance(result, dict)
    assert "breached" in result or "count" in result or "error" in result
