"""Project commands exposed through ``uv run``."""

from __future__ import annotations

import subprocess
import sys

DEV_BOOK = "book.dev.yml"


def _run(command: str, *args: str) -> None:
    subprocess.run([command, *args], check=True)


def _book(*args: str) -> None:
    _run("marimo-book", *args)


def dev() -> None:
    """Start the marimo-book development server."""
    _book("serve", "--book", DEV_BOOK)


def edit() -> None:
    """Open marimo's home page for content or a requested notebook."""
    targets = sys.argv[1:]
    _run("marimo", "edit", *(targets or ["content/"]))


def build() -> None:
    """Build the book and fail on warnings."""
    _book("build", "--book", DEV_BOOK, "--strict")


def check() -> None:
    """Validate the book configuration and table of contents."""
    _book("check", "--book", "book.yml", "--strict")


def clean() -> None:
    """Remove generated book artifacts."""
    _book("clean")


def release() -> None:
    """Perform a clean, strict production build."""
    _book("build", "--book", "book.yml", "--clean", "--strict")
