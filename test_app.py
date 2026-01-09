"""Tests for app.py"""

from app import hello

def test_hello():
    assert hello() == "Hello from XOR Verifier Sandbox"

if __name__ == "__main__":
    test_hello()
    print("All tests pass!")
