"""Testing for dictionary utility functions."""


from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count



def test_invert() -> None:
    """Tests invert function for use case."""
    xs: dict[str, str] = {"a": "one", "b": "two", "c": "three"}
    assert invert(xs) == {"one": "a", "two": "b", "three": "c"}


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
    xs: list[str] = ["blue", "blue", "green", "red"]
    assert count(xs) == {"blue": 3, "green": 1, "red": 1}