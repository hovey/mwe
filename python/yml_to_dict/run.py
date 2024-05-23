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


# loop method
city_names = db["state"]["cities"].keys()
cities = []  # accumlator
for city, item in zip(city_names, db["state"]["cities"].values()):

    cc = City(name=city, population=item["population"], nickname=item["nickname"])
    cities.append(cc)

    print(cc)

nm = State(name=db["state"]["name"], cities=cities)

print(f"{nm.name} has the following cities:")
for item in nm.cities:
    print(f"{item.name}, population: {item.population}, nickname: {item.nickname}")


# leaves, branches, then trunk
# list comprehension method
cities_lc = [
    City(name=x, population=y["population"], nickname=y["nickname"])
    for (x, y) in zip(db["state"]["cities"].keys(), db["state"]["cities"].values())
]

assert nm.cities == cities_lc

nm2 = State(name=db["state"]["name"], cities=cities_lc)

assert nm2 == nm

# all-at-once
# list comprehension method
nm3 = State(
    name=db["state"]["name"],
    cities=[
        City(name=x, population=y["population"], nickname=y["nickname"])
        for (x, y) in zip(db["state"]["cities"].keys(), db["state"]["cities"].values())
    ],
)

assert nm3 == nm

# breakpoint()
