"""This module demonstrates reading in a yml file into a dictionary,
and creating various NamedTuples from the dictionary."""

from typing import Final, NamedTuple

import yaml

FIN: Final[str] = "example.yml"

print(f"processing file: {FIN}")

db = []  # empty database

try:
    with open(file=FIN, mode="r", encoding="utf-8") as stream:
        db = yaml.load(stream, Loader=yaml.SafeLoader)  # overwrite
except yaml.YAMLError as error:

    print(f"Error with yml module: {error}")
    print(f"Could not open or decode: {FIN}")
    raise OSError from error


print(f"\nSuccess: database created from file: {FIN}")
print("key, value, type")
print("---, -----, ----")
for key, value in db.items():
    print(f"{key}, {value}, {type(value)}")

print(db)


class City(NamedTuple):
    """A basic definition of a City structure."""

    name: str
    population: int
    nickname: str


class State(NamedTuple):
    """A basic definition of a State structure."""

    name: str
    cities: list[City]


# ---------------------
# Method 1: loop method
# ---------------------
city_names_v1 = db["state"]["cities"].keys()
cities_v1 = []  # accumlator
for city, item in zip(city_names_v1, db["state"]["cities"].values()):

    cc = City(name=city, population=item["population"], nickname=item["nickname"])
    cities_v1.append(cc)

    print(cc)

state_v1 = State(name=db["state"]["name"], cities=cities_v1)

print(f"{state_v1.name} has the following cities:")
for item in state_v1.cities:
    print(f"{item.name}, population: {item.population}, nickname: {item.nickname}")


# -----------------------------------
# Method 2: list comprehension method
# leaves, branches, then trunk
# -----------------------------------

cities_v2 = [
    City(name=x, population=y["population"], nickname=y["nickname"])
    for (x, y) in zip(db["state"]["cities"].keys(), db["state"]["cities"].values())
]

assert cities_v2 == state_v1.cities

state_v2 = State(name=db["state"]["name"], cities=cities_v2)

assert state_v2 == state_v1

# -------------------------
# Method 3: all-at-once
# list comprehension method
# -------------------------
state_v3 = State(
    name=db["state"]["name"],
    cities=[
        City(name=x, population=y["population"], nickname=y["nickname"])
        for (x, y) in zip(db["state"]["cities"].keys(), db["state"]["cities"].values())
    ],
)

assert state_v3 == state_v1

# ------------------------------------------------------
# Method 4: dictionary unpacking with list comprehension
# pythonic dictionary to namedtuple
# ------------------------------------------------------

# cc = [
#     City(name=x, population=y["population"], nickname=y["nickname"])
#     for (x, y) in zip(db["state"]["cities"].keys(), db["state"]["cities"].values())
# ]

state_v4 = State(
    name=db["state"]["name"],
    cities=[
        City(**y)
        for y in [
            {
                "name": x,
                "population": db["state"]["cities"][x]["population"],
                "nickname": db["state"]["cities"][x]["nickname"],
            }
            for x in db["state"]["cities"].keys()
        ]
    ],
)

assert state_v4 == state_v1

# breakpoint()
#
# aa = 4
