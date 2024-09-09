"""Static checks"""

from subprocess import run
from typing import Final

PKGS: Final[list[str]] = [
    "tests",
    "generate_compose",
    "rpms_signature_scan",
    "clean_spacerequests",
]


def test_mypy() -> None:
    """Static Type check"""
    run(["mypy"] + PKGS, check=True)


def test_isort() -> None:
    """Imports formatting check"""
    run(["isort", "--check", "--profile", "black"] + PKGS, check=True)


def test_black() -> None:
    """Formatting check"""
    run(["black", "--check"] + PKGS, check=True)


def test_pylint() -> None:
    """Lint check"""
    run(["pylint"] + PKGS, check=True)
