__all__ = ["greet"]


def greet(name: str = "world") -> str:
    return f"hello, {name}"
