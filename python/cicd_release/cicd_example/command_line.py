"""Illustration of command line entry points."""

from typing import Final

BANNER: Final[
    str
] = """-------------------------------
This is the cicd_example module
-------------------------------
"""


CLI_DOCS: Final[
    str
] = """cicd_example
    (this command)

hello
    Runs the 'Hello world!' example.

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


def renumber(source: tuple, old: tuple, new: tuple) -> tuple:
    """Given a source tuple, composed of a list of positive integers,
    a tuple of `old` numbers that maps into `new` numbers, return the
    source tuple with the `new` numbers."""
    result = ()
    for item in source:
        idx = old.index(item)
        new_value = new[idx]
        result = result + (new_value,)

    return result


def mesh_element_connectivity(mesh_lattice_connectivity: tuple):
    """Given a mesh with lattice connectivity, return a mesh with finite
    element connectivity.
    """
    # create a list of unordered lattice node numbers
    ln = []
    for item in mesh_lattice_connectivity:
        print(f"item is {item}")
        # The first item is the block number
        # block = item[0]
        # The second and onward items are the elements
        elements = item[1:]
        for element in elements:
            ln += list(element)

    ln_set = set(ln)  # sets are not necessarily ordered
    ln_ordered = tuple(sorted(ln_set))  # now these unique integers are ordered

    # and they will map into the new compressed unique interger list `mapsto`
    mapsto = tuple(range(1, len(ln_ordered)+1))

    # now build a mesh_with_element_connectivity
    mesh = ()  # empty tuple
    # breakpoint()
    for item in mesh_lattice_connectivity:
        # The first item is the block number
        block_number = item[0]
        block_and_elements = ()  # empty tuple
        # insert the block number
        block_and_elements = block_and_elements + (block_number,)
        for element in item[1:]:
            new_element = renumber(source=element, old=ln_ordered, new=mapsto)
            # overwrite
            block_and_elements = block_and_elements + (new_element,)

        mesh = mesh + (block_and_elements,)  # overwrite

    return mesh


def elements_without_block_ids(mesh: tuple) -> tuple:
    """Given a mesh, removes the block ids and returns only just the
    element connectivities.
    """

    aa = ()
    for item in mesh:
        bb = item[1:]
        aa = aa + bb

    return aa
