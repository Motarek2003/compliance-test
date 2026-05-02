"""Minimal Python source so CodeQL has something to analyze."""

import subprocess
import sys


def greet(name: str) -> str:
    return f"Hello, {name}!"


def run_user_expression(expr: str):
    # VULNERABLE (intentional, for CodeQL test): py/code-injection
    return eval(expr)


def run_user_command(cmd: str):
    # VULNERABLE (intentional, for CodeQL test): py/shell-command-constructed-from-input
    return subprocess.call(cmd, shell=True)


if __name__ == "__main__":
    print(greet("CloudSentry"))
    if len(sys.argv) > 1:
        # Tainted source -> dangerous sink
        run_user_expression(sys.argv[1])
        run_user_command(sys.argv[1])
