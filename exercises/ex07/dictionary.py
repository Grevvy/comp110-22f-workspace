"""Dictionary function utilities."""

__author__ = "730529974"


def invert(xs: dict[str, str]) -> dict[str, str]:
    """Reverses they keys and values in a dictionary from key, value to value, key."""
    result: dict[str, str] = {}
    for keys in xs:
        if xs[keys] in result:
            raise KeyError("Cannot have the same value twice.")
        else:
            result[xs[keys]] = keys
    return result


def favorite_color(xs: dict[str, str]) -> str:
    """Determines the favorite color of a group of people."""
    result: dict[str, int] = {}
    fav_color: str = ""
    color_count: int = 0
    for keys in xs:
        cur_color = xs[keys]
        if cur_color in result:
            result[xs[keys]] += 1
        else:
            result[xs[keys]] = 1
    for keys in result:
        if color_count < result[keys]:
            color_count = result[keys]
            fav_color = keys
    return fav_color


def count(xs: list[str]) -> dict[str, int]:
    """Creates a dictionary that has the items as keys and the number of times that item occurs."""
    ks: dict[str, int] = {}
    i: int = 0
    while i < len(xs):
        if xs[i] in ks:
            ks[xs[i]] += 1
        else:
            ks[xs[i]] = 1
        i += 1
    return ks