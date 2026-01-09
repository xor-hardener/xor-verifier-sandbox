"""Clean, well-written code as a control for ABILITY-004 testing."""

from __future__ import annotations

import hashlib
import os
from typing import Any


def safe_hash(data: str) -> str:
    """Compute SHA-256 hash of input string."""
    return hashlib.sha256(data.encode()).hexdigest()


def get_env_var(name: str, default: str | None = None) -> str | None:
    """Safely retrieve environment variable."""
    return os.environ.get(name, default)


def sanitize_input(user_input: str) -> str:
    """Sanitize user input by removing dangerous characters."""
    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-")
    return "".join(c for c in user_input if c in allowed_chars)


def process_data(data: dict[str, Any]) -> dict[str, Any]:
    """Process data safely with validation."""
    if not isinstance(data, dict):
        raise TypeError("Expected dict input")
    
    return {
        "processed": True,
        "item_count": len(data),
    }
