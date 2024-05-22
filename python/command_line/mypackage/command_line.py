"""Illustration of command line entry points."""

from typing import Final

BANNER: Final[
    str
] = """----------------------------
This is the mypackage module
----------------------------
"""


CLI_DOCS: Final[
    str
] = """mypackage
    (this command)

hello
    Runs the 'Hello World!' example.

pytest
    Runs the test suite (non-verbose option).

pytest -v
    Runs the test suite (verbose option).
"""


def mymodule():
    """Prints the command line documentation to the command window."""
    print(BANNER)
    print(CLI_DOCS)


def hello() -> str:
    """Simple example of a function hooked to a command line entry point.

    Returns:
        The canonical "Hello world!" string.
    """

    return "Hello world!"
