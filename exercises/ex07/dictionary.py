"""Dictionary function utilities."""

__author__ = "730529974"


from re import X


def invert(xs: dict[str, str]) -> dict[str,str]:
    """reverses they keys and values in a dictionary from key, value to value, key."""
    result: dict[str, str] = {}
    for keys in xs:
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


def count(xs: list[str]) -> dict[str,int]:
    ks: dict[str,int] = {}
    i: int = 0
    # add items from a list into a dictionary as keys
    # if multiple keys exist increase the value by 1
    for x in xs:
        for keys in ks:
            x = keys
            if x in ks:
                ks[keys] += 1
            else:
                ks[keys] = 1
    return ks

print(count(["blue", "blue", "green", "red"]))