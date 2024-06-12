# to generate the coverage report
# pytest --cov=.
# pytest --cov=. --cov-report=html


def hello() -> str:
    """Hello world in English."""
    return "Hello World!"


def hola() -> str:
    """Hello world in Spanish."""
    return "Hola Mundo!"


# in source_1 only
# def test_hello():
#     assert hello() == "Hello World!"


# in source_2 only
def test_hola():
    assert hola() == "Hola Mundo!"
