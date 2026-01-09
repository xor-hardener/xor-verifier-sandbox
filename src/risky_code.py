"""Risky code for ABILITY-004 guardrail testing."""

import os
import subprocess
import pickle


def unsafe_eval(user_input: str):
    """INTENTIONAL: Dangerous eval for testing."""
    return eval(user_input)


def unsafe_shell(cmd: str):
    """INTENTIONAL: Shell injection vulnerability."""
    return subprocess.run(cmd, shell=True, capture_output=True)


def unsafe_pickle(data: bytes):
    """INTENTIONAL: Unsafe deserialization."""
    return pickle.loads(data)


def hardcoded_secret():
    """INTENTIONAL: Hardcoded credential."""
    api_key = "sk-test-1234567890abcdef"
    return api_key


def sql_injection(user_id: str):
    """INTENTIONAL: SQL injection vulnerability."""
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    return query
