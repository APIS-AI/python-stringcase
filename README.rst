stringcase
==========

Lightweight string case conversion helpers for Python.

The module provides a small, dependency-free API for converting strings between
common naming styles such as camel case, snake case, spinal case, path case,
and title case.

Installation
------------

::

    pip install stringcase

Usage
-----

.. code:: python

    import stringcase

    stringcase.camelcase("foo_bar_baz")    # "fooBarBaz"
    stringcase.pascalcase("foo.bar.baz")   # "FooBarBaz"
    stringcase.snakecase("FooBarBaz")      # "foo_bar_baz"
    stringcase.spinalcase("FooBarBaz")     # "foo-bar-baz"
    stringcase.pathcase("FooBarBaz")       # "foo/bar/baz"
    stringcase.titlecase("foo_bar_baz")    # "Foo Bar Baz"
    stringcase.alphanumcase("Foo_123!")    # "Foo123"

Available helpers
-----------------

- ``camelcase``
- ``capitalcase``
- ``constcase``
- ``lowercase``
- ``pascalcase``
- ``pathcase``
- ``backslashcase``
- ``sentencecase``
- ``snakecase``
- ``spinalcase``
- ``dotcase``
- ``titlecase``
- ``trimcase``
- ``uppercase``
- ``alphanumcase``

Testing
-------

::

    pytest -q

License
-------

This project is released under the MIT License. See ``LICENSE`` for details.
