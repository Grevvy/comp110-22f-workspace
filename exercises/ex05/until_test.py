"""Testing for list utility functions."""


from exercises.ex05.utils import only_evens
from exercises.ex05.utils import concat
from exercises.ex05.utils import sub


def test_only_evens() -> None:
    """Tests an empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_all_evens() -> None:
    """Tests only_evens function if all numbers are even."""
    xs: list[int] = [2, 2, 2] 
    assert only_evens(xs) == [2, 2, 2]


def test_only_evens_all_odd() -> None:
    """Test only_evens function if all numbers are odd."""
    xs: list[int] = [1, 3, 5]
    assert only_evens(xs) == []


def test_only_evens_use_case() -> None:
    """Tests a regular use case for the only_evens function."""
    xs: list[int] = [1, 2, 3, 4]
    assert only_evens(xs) == [2, 4]


def test_concat_empty_lists() -> None:
    """Tests the concat function if both lists are empty."""
    xs: list[int] = []
    xa: list[int] = []
    assert concat(xs, xa) == []


def test_concat_use_case() -> None:
    """Tests concat function for normal use case."""
    xs: list[int] = [1, 2, 3]
    xa: list[int] = [4, 5, 6]
    assert concat(xs, xa) == [1, 2, 3, 4, 5, 6]


def test_concat_use_case_two() -> None:
    """Tests concat function of a use case but reversed order of numbers."""
    xs: list[int] = [4, 5, 6]
    xa: list[int] = [1, 2, 3]
    assert concat(xs, xa) == [4, 5, 6, 1, 2, 3]


def test_sub_use_case() -> None:
    """Tests the sub for a regular use case."""
    xs: list[int] = [10, 20, 30, 40, 50]
    a: int = 1
    b: int = 4
    assert sub(xs, a, b) == [20, 30, 40]


def test_sub_start_negative() -> None:
    """Tests sub function if the first parameter is negative."""
    xs: list[int] = [10, 20, 30, 40]
    a: int = -2
    b: int = 3
    assert sub(xs, a, b) == [10, 20, 30]


def test_sub_end_too_long() -> None:
    """Tests that is the end parameter is too long, the end parameter becomes the length of the list."""
    xs: list[int] = [10, 20, 30, 40]
    a: int = 0
    b: int = 5
    assert sub(xs, a, b) == [10, 20, 30, 40]


def test_sub_length_zero() -> None:
    """Tests is the list given is empty, return an empty list."""
    xs: list[int] = []
    a: int = 0
    b: int = 1
    assert sub(xs, a, b) == []


def test_sub_start_outside_list() -> None:
    """Tests if the start parameter is outside the length of the list, return an empty list."""
    xs: list[int] = [10, 20, 30]
    a: int = 4
    b: int = 5
    assert sub(xs, a, b) == []


def test_sub_end_zero() -> None:
    """Tests if the end parameter is zero, return an empty list."""
    xs: list[int] = [10, 20, 30]
    a: int = 0
    b: int = 0
    assert sub(xs, a, b) == []