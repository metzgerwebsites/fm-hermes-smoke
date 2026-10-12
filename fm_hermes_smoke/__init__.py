"""Minimal package for the fm-hermes-smoke acceptance suite."""

__all__ = ["smoke_message"]

__version__ = "0.1.0"


def smoke_message() -> str:
    """Return the package's smoke identifier."""
    return "fm-hermes-smoke"