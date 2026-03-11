"""Public string case conversion helpers."""

from __future__ import annotations

import re


# ---------------------------------------------------------------------------
# Internal helper
# ---------------------------------------------------------------------------

def _tokenize(string: object) -> list[str]:
    """Split an arbitrary string into lowercase word tokens.

    Handles snake_case, kebab-case, space-separated, and PascalCase/camelCase
    inputs uniformly.
    """
    s: str = str(string)
    # Insert a separator before each uppercase letter that follows a lowercase
    # letter or digit (camelCase / PascalCase boundary).
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s)
    # Replace any run of non-alphanumeric characters with a single separator.
    s = re.sub(r"[^a-zA-Z0-9]+", "_", s)
    # Strip leading/trailing separators and split.
    tokens: list[str] = [t for t in s.strip("_").split("_") if t]
    return [t.lower() for t in tokens]


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def camelcase(string: object) -> str:
    """Convert *string* to camelCase."""
    tokens: list[str] = _tokenize(string)
    if not tokens:
        return ""
    return tokens[0] + "".join(t.capitalize() for t in tokens[1:])


def capitalcase(string: object) -> str:
    """Capitalise the first character of *string*, leaving the rest as-is."""
    s: str = str(string)
    if not s:
        return ""
    return s[0].upper() + s[1:]


def constcase(string: object) -> str:
    """Convert *string* to CONST_CASE (SCREAMING_SNAKE_CASE)."""
    return "_".join(t.upper() for t in _tokenize(string))


def lowercase(string: object) -> str:
    """Return *string* converted to all lower-case characters."""
    return str(string).lower()


def pascalcase(string: object) -> str:
    """Convert *string* to PascalCase."""
    return "".join(t.capitalize() for t in _tokenize(string))


def pathcase(string: object) -> str:
    """Convert *string* to path/case (forward-slash separated, lower-case)."""
    tokens: list[str] = _tokenize(string)
    if not tokens:
        return ""
    return "/".join(tokens)


def backslashcase(string: object) -> str:
    r"""Convert *string* to back\slash\case (backslash separated, lower-case)."""
    tokens: list[str] = _tokenize(string)
    if not tokens:
        return ""
    return "\\".join(tokens)


def sentencecase(string: object) -> str:
    """Convert *string* to Sentence case."""
    tokens: list[str] = _tokenize(string)
    if not tokens:
        return ""
    sentence: str = " ".join(tokens)
    return sentence[0].upper() + sentence[1:]


def snakecase(string: object) -> str:
    """Convert *string* to snake_case."""
    return "_".join(_tokenize(string))


def spinalcase(string: object) -> str:
    """Convert *string* to spinal-case (kebab-case)."""
    return "-".join(_tokenize(string))


def dotcase(string: object) -> str:
    """Convert *string* to dot.case."""
    return ".".join(_tokenize(string))


def titlecase(string: object) -> str:
    """Convert *string* to Title Case."""
    return " ".join(t.capitalize() for t in _tokenize(string))


def trimcase(string: object) -> str:
    """Strip leading and trailing whitespace from *string*."""
    return str(string).strip()


def uppercase(string: object) -> str:
    """Return *string* converted to all upper-case characters."""
    return str(string).upper()


def alphanumcase(string: object) -> str:
    """Strip all non-alphanumeric characters from *string*."""
    return re.sub(r"[^a-zA-Z0-9]", "", str(string))
