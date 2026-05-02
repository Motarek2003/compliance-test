"""Minimal Python source so CodeQL has something to analyze."""


def greet(name: str) -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("CloudSentry"))
