"""Testing for dictionary utility functions."""


from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count



def test_invert() -> None:
    """Tests invert function for use case."""
    xs: dict[str, str] = {"a": "one", "b": "two", "c": "three"}
    assert invert(xs) == {"one": "a", "two": "b", "three": "c"}


def test_invert_empty() -> None:
    """Tests invert function if argument is empty."""
    xs: dict[str, str] = {}
    assert invert(xs) == {}


def test_invert_same() -> None:
    """Tests what happens if argument has two of the same values."""
    xs: dict[str, str] = {"a": "one", "b": "one"}
    assert invert(xs) == {"one": "b"}


def test_favorite_color() -> None:
    """Test favorite color function for use case."""
    xs: dict[str, str] = {"jim": "blue", "john": "blue", "joe": "yellow", "Jane": "green"}
    assert favorite_color(xs) == "blue"


def test_favorite_color_all_one() -> None:
    """Test function returns the first value if they are all shown once."""
    xs: dict[str, str] = {"jim": "red", "john": "yellow", "joe": "blue"}
    assert favorite_color(xs) == "red"


def test_favorite_color_empty() -> None:
    """If the argument is empty, returns nothing"""
    xs: dict[str, str] = {}
    assert favorite_color(xs) == ""


def test_count() -> None:
    """Test count for use case."""
    xs: list[str] = ["blue", "blue", "green", "green", "red"]
    assert count(xs) == {"blue": 2, "green": 2, "red": 1}


def test_count_empty() -> None:
    """Test count function if argument is empty."""
    xs: list[str] = []
    assert count(xs) == {}


def test_count_all_same() -> None:
    """Test count function if argument is all the same item."""
    xs: list[str] = ["green", "green", "green", "green"]
    assert count (xs) == {"green": 4}