"""This module returns the coordinates and connectivity patterns for
quadrilateral and hexahedral elements.
"""

import itertools
from typing import NamedTuple


class Point2D(NamedTuple):
    """A physical (integer) point in R2."""

    x: int
    y: int


class Point3D(NamedTuple):
    """A physical (integer) point in R3."""

    x: int
    y: int
    z: int


# Type alias for functional style methods
# https://docs.python.org/3/library/typing.html#type-aliases


class Quad(NamedTuple):
    """A single quadrilateral element."""

    sw: Point2D
    se: Point2D
    ne: Point2D
    nw: Point2D


class Hex(NamedTuple):
    """A single hexahedral element."""

    # The 'a' set
    swa: Point2D
    sea: Point2D
    nea: Point2D
    nwa: Point2D
    # The 'b' set
    swb: Point2D
    seb: Point2D
    neb: Point2D
    nwb: Point2D


def QuadMesh(NamedTuple):
    """A mesh composed of quadrilateral elements."""
    # coordinates: tuple(Quad, ...)
    pass


def HexMesh(NamedTuple):
    """A mesh composed of hexahedral elements."""
    pass


def flatten(list_of_lists):
    "Flatten one level of nesting."
    return itertools.chain.from_iterable(list_of_lists)


# def process(nelx: int, nely: int, nelz: int) -> QuadMesh | HexMesh:
def process(nelx: int, nely: int, nelz: int):
    """Returns the integer coordinates and connectivity for a quadrilateral (2D)
    or hexahedral (3D) mesh.

    nelx: The number of elements along the x-axis.
    nely: The number of elements along the y-axis.
    nelz: The number of elements along the z-axis, 0 if 2D.

    """
    if nelz == 0:
        nnp = (nelx + 1) * (nely + 1)  # number of nodal points
        # nn = tuple(range(1, nnp + 1))  # node numbers
        # nnr = tuple(reversed(range(1, nnp + 1)))  # node numbers reversed
        row_x = tuple(range(nelx))
        row_y = tuple(0 for x in range(nelx))
        xs = tuple(row_x for y in range(nely + 1))
        x = tuple(flatten(xs))
        ys = tuple(map(lambda y: tuple(itertools.repeat(y, nelx)), range(nely + 1)))
        # ys = tuple(map(lambda y: itertools.repeat(y, nelx), range(nely + 1)))
        y = tuple(flatten(ys))
        coordinates = tuple(zip(x, y))

        # seed = (0, 1, nelx + 2, nelx + 1)
        # seed = (0, 1, nelx + 1, nelx)
        # seed = (1, 2, nelx + 3, nelx + 2)
        seed = (0, 1, 3, 2)
        # tuple(tuple(x + y for x in (0, 1, 3, 2)) for y in range(1, nelx*nely + 1))
        # connectivity
        aa = tuple(tuple(map(lambda e: e + x, (0, 1, 3, 2))) for x in (1, 2))
        net = tuple(tuple(x + y for x in seed) for y in range(1, nelx * nely + 1))
        zz = []
        for y in range(nely):
            for x in range(nelx):
                print(f"(x, y) = ({x}, {y})")
                cc = 1 + x + y * nelx
                breakpoint()
        breakpoint()
        return QuadMesh

    # otherwise nelz>=1, then a 3D mesh

    return HexMesh


def test_single_quad():
    """Tests the pattern for a single quadrilateral element.

    nsd = 2
    nelx = nely = 1
       y
       ^
      3|      4
       *-----*
       |4   3|
       | (1) |
       |1   2|
       *-----* --> x
      1       2
    coordinates
    0, 0
    1, 0
    0, 1
    1, 1
    connectivity
    1 2 4 3
    """
    known_coor = (((0, 0), (1, 0), (0, 1), (1, 1)),)
    known_conn = ((1, 2, 4, 3),)

    found = process(nelx=2, nely=2, nelz=0)
