"""List utilities."""

__author__ = "730529974"


def only_evens(xs: list[int]) -> list[int]:
    """Determins if a list contains only even numbers."""
    a: list[int] = []
    for x in xs:
        if x % 2 == 0:
            a.append(x)
    return a         


def concat(xs: list[int], xa: list[int]) -> list[int]:
    """Adds items from a second list to the first."""
    a: list[int] = []
    for x in xs:
        a.append(x)
    for x in xa:
        a.append(x)
    return a


def sub(xs: list[int], a: int, b: int) -> list[int]:
    """Given a set limit in an index. returns the values in the list between the two parameters."""
    c: list[int] = []
    if len(xs) < 1:
        return c
    if a >= len(xs):
        return c
    while a < b:
        if a < 0:
            a = 0
        if b > len(xs):
            b = len(xs)
        x: int = xs[a]
        if x == xs[a]:
            c.append(x)
        a += 1
    return c