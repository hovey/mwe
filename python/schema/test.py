"""This module runs a Schema test from https://pypi.org/project/schema/"""

import pdbp  # colorized debugger with pip install pdbp

from schema import Schema, And, Use, Optional, SchemaError

schema = Schema(
    [
        {
            "name": And(str, len),
            "age": And(Use(int), lambda n: 18 <= n <= 99),
            Optional("gender"): And(
                str,
                Use(str.lower),
                lambda s: s in ("squid", "kid"),
            ),
        }
    ]
)

data = [
    {"name": "Sue", "age": "28", "gender": "Squid"},
    {"name": "Sam", "age": "42"},
    {"name": "Sacha", "age": "20", "gender": "KID"},
]

# if data is valid, Schema.validate will return the validated data,
# if data is invalid, Schema.validate will raise a SchemaError exception.
validation_1 = schema.validate(data)

assert validation_1 == [
    {"name": "Sue", "age": 28, "gender": "squid"},
    {"name": "Sam", "age": 42},
    {"name": "Sacha", "age": 20, "gender": "kid"},
]

print("First tests are valid.")

bad_data = [
    {"name": "Sue", "age": "18", "gender": "Squid"},
    {"name": "Sam", "age": "90"},
    {"name": "Sacha", "age": "20", "gender": "unknown"},
]

validation_2 = schema.validate(bad_data)

breakpoint()

print("Second tests are valid.")
