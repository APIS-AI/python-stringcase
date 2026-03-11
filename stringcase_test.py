"""Tests for stringcase."""

from stringcase import (
    camelcase,
    capitalcase,
    constcase,
    lowercase,
    pascalcase,
    pathcase,
    sentencecase,
    uppercase,
    snakecase,
    spinalcase,
    titlecase,
    trimcase,
    alphanumcase,
)


def test_camelcase() -> None:
    assert camelcase("foo_bar_baz") == "fooBarBaz"
    assert camelcase("FooBarBaz") == "fooBarBaz"
    assert camelcase("foo-bar-baz") == "fooBarBaz"
    assert camelcase("foo bar baz") == "fooBarBaz"
    assert camelcase("") == ""
    assert camelcase("foo") == "foo"


def test_capitalcase() -> None:
    assert capitalcase("foo bar") == "Foo bar"
    assert capitalcase("FOO BAR") == "FOO BAR"
    assert capitalcase("") == ""
    assert capitalcase("f") == "F"
    assert capitalcase("foo") == "Foo"


def test_constcase() -> None:
    assert constcase("foo_bar_baz") == "FOO_BAR_BAZ"
    assert constcase("FooBarBaz") == "FOO_BAR_BAZ"
    assert constcase("foo-bar-baz") == "FOO_BAR_BAZ"
    assert constcase("foo bar baz") == "FOO_BAR_BAZ"
    assert constcase("") == ""


def test_lowercase() -> None:
    assert lowercase("FOO BAR") == "foo bar"
    assert lowercase("FooBar") == "foobar"
    assert lowercase("") == ""
    assert lowercase("ABC") == "abc"


def test_pascalcase() -> None:
    assert pascalcase("foo_bar_baz") == "FooBarBaz"
    assert pascalcase("FooBarBaz") == "FooBarBaz"
    assert pascalcase("foo-bar-baz") == "FooBarBaz"
    assert pascalcase("foo bar baz") == "FooBarBaz"
    assert pascalcase("") == ""
    assert pascalcase("foo") == "Foo"


def test_pathcase() -> None:
    assert pathcase("foo_bar_baz") == "foo/bar/baz"
    assert pathcase("FooBarBaz") == "foo/bar/baz"
    assert pathcase("foo-bar-baz") == "foo/bar/baz"
    assert pathcase("foo bar baz") == "foo/bar/baz"
    assert pathcase("") == ""


def test_sentencecase() -> None:
    assert sentencecase("foo_bar_baz") == "Foo bar baz"
    assert sentencecase("FooBarBaz") == "Foo bar baz"
    assert sentencecase("foo-bar-baz") == "Foo bar baz"
    assert sentencecase("foo bar baz") == "Foo bar baz"
    assert sentencecase("") == ""


def test_uppercase() -> None:
    assert uppercase("foo bar") == "FOO BAR"
    assert uppercase("FooBar") == "FOOBAR"
    assert uppercase("") == ""
    assert uppercase("abc") == "ABC"


def test_snakecase() -> None:
    assert snakecase("foo_bar_baz") == "foo_bar_baz"
    assert snakecase("FooBarBaz") == "foo_bar_baz"
    assert snakecase("foo-bar-baz") == "foo_bar_baz"
    assert snakecase("foo bar baz") == "foo_bar_baz"
    assert snakecase("") == ""


def test_spinalcase() -> None:
    assert spinalcase("foo_bar_baz") == "foo-bar-baz"
    assert spinalcase("FooBarBaz") == "foo-bar-baz"
    assert spinalcase("foo-bar-baz") == "foo-bar-baz"
    assert spinalcase("foo bar baz") == "foo-bar-baz"
    assert spinalcase("") == ""


def test_titlecase() -> None:
    assert titlecase("foo bar baz") == "Foo Bar Baz"
    assert titlecase("foo_bar_baz") == "Foo Bar Baz"
    assert titlecase("FooBarBaz") == "Foo Bar Baz"
    assert titlecase("") == ""


def test_trimcase() -> None:
    assert trimcase("  foo bar  ") == "foo bar"
    assert trimcase("foo bar") == "foo bar"
    assert trimcase("") == ""
    assert trimcase("   ") == ""


def test_alphanumcase() -> None:
    assert alphanumcase("foo_bar-baz!") == "foobarbaz"
    assert alphanumcase("hello world 123") == "helloworld123"
    assert alphanumcase("!@#$%^&*()") == ""
    assert alphanumcase("abc123") == "abc123"
    assert alphanumcase("") == ""
