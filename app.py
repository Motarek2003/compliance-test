"""Minimal Python source so CodeQL has something to analyze."""

import hashlib
import subprocess
import sys

import requests


def greet(name: str) -> str:
    return f"Hello, {name}!"


def hash_password(password: str) -> str:
    # VULNERABLE (intentional, for CodeQL test): py/weak-sensitive-data-hashing (MD5)
    return hashlib.md5(password.encode()).hexdigest()


def fetch_unverified(url: str):
    # VULNERABLE (intentional, for CodeQL test): py/request-without-cert-validation
    return requests.get(url, verify=False, timeout=5)


def run_user_expression(expr: str):
    # VULNERABLE (intentional): py/code-injection
    return eval(expr)


def run_user_command(cmd: str):
    # VULNERABLE (intentional): py/shell-command-constructed-from-input
    return subprocess.call(cmd, shell=True)


if __name__ == "__main__":
    print(greet("CloudSentry"))
    print(hash_password("secret123"))
    if len(sys.argv) > 1:
        run_user_expression(sys.argv[1])
        run_user_command(sys.argv[1])
        fetch_unverified(sys.argv[1])
