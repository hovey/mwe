"""This module returns the coordinates and connectivity patterns for
quadrilateral and hexahedral elements.

    ^ Y
    |
  y +-----+-----+-----+ ... +-----+ ... +-----+ (x*y), nnp = (x+1)*(y+1)
    |     |     |     |     |     |     |     |
    |     |     |     |     |     |     |     |
    +-----+-----+-----+ ... +-----+ ... +-----+
    .
    .
  3 +-----+-----+ ...   j+1 +-----+ ... +-----+
    |     |     |           |     |     |     |
    |     |     |           |     |     |     |
  2 +-----+-----+ ...     j +-----+ ... +-----+
                            i    i+1

   x+1   x+2   x+3   x+4
  1 +-----+-----+-----+ ... +-----+ ... d-----c (nx*ny) -> (2nx)
    |     |     |     |     |     |     |     |
    |  1  |  2  |  3  |     |     |     |     |
  0 1-----2-----3-----4 ... +-----+ ... a-----b --> X
    0     1     2     3                       x

    a = x-1 + y*nex
    b = x   + y*nex
    c = x+2 + y*nex
    d = x+1 + y*nex

    ----------
    3 . 4         4 . 5 . 6 .    5 . 6 . 7 . 8
    . 1 .         . 1 . 2 .      . 1 . 2 . 3 .
    1 . 2         1 . 2 . 3 .    1 . 2 . 3 . 4

    nx=1, ny=1    nx=2, ny=1     nx=3, ny=1
    1: 1 2 4 3    1: 1 2 5 4     1: 1 2 6 5
                  2: 2 3 6 5     2: 2 3 7 6
                                 3: 3 4 8 7
    ----------
    5 . 6         7 . 8 . 9 .    9 .10 .11 .12
    . 2 .         . 3 . 4 .      . 4 . 5 . 6 .
    3 . 4         4 . 5 . 6      5 . 6 . 7 . 8
    . 1 .         . 1 . 2 .      . 1 . 2 . 3 .
    1 . 2         1 . 2 . 3      1 . 2 . 3 . 4

    nx=1, ny=2    nx=2, ny=2     nx=3, ny=2
    1: 1 2 4 3    1: 1 2 5 4     1: 1 2 6 5
    2: 3 4 6 5    2: 2 3 6 5     2: 2 3 7 6
                  3: 4 5 8 7     3: 3 4 8 7
                  4: 5 6 9 8     4: 5 6 10 9
                                 5: 6 7 11 10
                                 6: 7 8 12 11

"""

import itertools
from typing import NamedTuple

import pdbp  # colorized debugging


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


def quilt(*, nex: int, ney: int):
    """Given a grid of nex elements in the x-axis and ney elements in the
    y, axis, returns the element numbers as a list of list by row (x-axis)."""
    count = 0
    elements = []
    for _ in range(ney):
        row = []
        for i in range(nex):
            count += 1
            row.append(count)
        elements.append(row)

    count = 0
    nodes = []
    for _ in range(ney + 1):
        row = []
        for i in range(nex + 1):
            count += 1
            row.append(count)
        nodes.append(row)

    return [elements, nodes]


def connectivity(qq):
    """Given a quilt of element numbers and node numbers, return the
    element connectivity."""
    elements = []
    e = 0
    ney = len(qq[0])
    nex = len(qq[0][0])
    ns = qq[1]  # nodes, as a list of global node numbers
    # nel = nex * ney

    for j in range(ney):
        # row = []
        for i in range(nex):
            e += 1  # global element number
            # row.append([e, ns[j][i], ns[j][i + 1], ns[j + 1][i + 1], ns[j + 1][i]])
            # local element numbers
            sw = ns[j][i]  # southwest
            se = ns[j][i + 1]  # southeast
            ne = ns[j + 1][i + 1]  # northeast
            nw = ns[j + 1][i]  # northwest
            # elements.append([e, ns[j][i], ns[j][i + 1], ns[j + 1][i + 1], ns[j + 1][i]])
            elements.append([e, sw, se, ne, nw])
        # elements.append(row)

    return elements


if __name__ == "__main__":
    result = quilt(nex=3, ney=2)
    print(result)

    result = connectivity(result)
    print(result)

    a, b = 1, 1
    r1 = quilt(nex=a, ney=b)
    assert r1 == [[[1]], [[1, 2], [3, 4]]]
    r2 = connectivity(r1)
    assert r2 == [[1, 1, 2, 4, 3]]

    a, b = 2, 1  # overwrite
    r1 = quilt(nex=a, ney=b)  # overwrite
    assert r1 == [[[1, 2]], [[1, 2, 3], [4, 5, 6]]]
    r2 = connectivity(r1)  # overwrite
    assert connectivity(r1) == [[1, 1, 2, 5, 4], [2, 2, 3, 6, 5]]

    a, b = 3, 1  # overwrite
    r1 = quilt(nex=a, ney=b)  # overwrite
    assert r1 == [[[1, 2, 3]], [[1, 2, 3, 4], [5, 6, 7, 8]]]
    r2 = connectivity(r1)  # overwrite
    assert connectivity(r1) == [[1, 1, 2, 6, 5], [2, 2, 3, 7, 6], [3, 3, 4, 8, 7]]

    a, b = 1, 2  # overwrite
    r1 = quilt(nex=a, ney=b)  # overwrite
    assert r1 == [[[1], [2]], [[1, 2], [3, 4], [5, 6]]]
    r2 = connectivity(r1)  # overwrite
    assert connectivity(r1) == [[1, 1, 2, 4, 3], [2, 3, 4, 6, 5]]

    a, b = 2, 2  # overwrite
    r1 = quilt(nex=a, ney=b)  # overwrite
    assert r1 == [[[1, 2], [3, 4]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
    r2 = connectivity(r1)  # overwrite
    assert connectivity(r1) == [
        [1, 1, 2, 5, 4],
        [2, 2, 3, 6, 5],
        [3, 4, 5, 8, 7],
        [4, 5, 6, 9, 8],
    ]

    a, b = 3, 2  # overwrite
    r1 = quilt(nex=a, ney=b)  # overwrite
    assert r1 == [[[1, 2, 3], [4, 5, 6]], [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]]
    r2 = connectivity(r1)  # overwrite
    assert connectivity(r1) == [
        [1, 1, 2, 6, 5],
        [2, 2, 3, 7, 6],
        [3, 3, 4, 8, 7],
        [4, 5, 6, 10, 9],
        [5, 6, 7, 11, 10],
        [6, 7, 8, 12, 11],
    ]


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
