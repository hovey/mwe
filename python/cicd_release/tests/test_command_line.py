""""This module tests the command_line services.

Example:
    To run
    cd ~/mwe/python/cicd_release
    activate the virutal environment, for example:
    source .venv/bin/activate.fish

    pytest (without code coverage)
    pytest mypackage/tests/test_command_line.py -v  # -v is for verbose

    to run just a single test in this module, for example
    pytest command_line/tests/test_command_line.py::test_hello_world -v
"""

from cicd_example import command_line as cl


def test_hello_world():
    """Tests that the string 'Hello world!' is returned."""
    print("test_hello_world...")
    fiducial = "Hello world!"

    found = cl.hello()

    assert found == fiducial
