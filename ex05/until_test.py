"""Testing for list utility functions."""


from ex05.utils import only_evens
from ex05.utils import concat
from ex05.utils import sub

def test_only_evens() -> None:
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_all_evens() -> None:
    xs: list[int] = [2, 2, 2] 
    assert only_evens(xs) == [2, 2, 2]


def test_only_evens_all_odd() -> None:
    xs: list[int] = [1, 3, 5]
    assert only_evens(xs) == []


def test_only_evens_use_case() -> None:
    xs: list[int] = [1, 2, 3 , 4]
    assert only_evens(xs) == [2, 4]


def test_concat_empty_lists() -> None:
    xs: list[int] = []
    xa: list[int] = []
    assert concat(xs, xa) == []


def test_concat_use_case() -> None:
    xs: list[int] = [1, 2, 3]
    xa: list[int] = [4, 5, 6]
    assert concat(xs, xa) == [1, 2, 3, 4, 5, 6]

def test_concat_use_case_two() -> None:
    xs: list[int] = [4, 5, 6]
    xa: list[int] = [1, 2, 3]
    assert concat(xs, xa) == [4, 5, 6, 1, 2, 3]


def test_sub_use_case() -> None:
    xs:list[int] = [10, 20, 30, 40, 50]
    a: int = 1
    b: int = 3
    assert sub(xs, 1, 4) == [20, 30, 40]


def test_sub_start_negative() -> None:
    xs: list[int] = [10, 20, 30, 40]
    a:int = -2
    b: int = 3
    assert sub(xs, a, b) == [10, 20, 30]

def test_sub_end_too_long() -> None:
    xs: list[int] = [10, 20, 30, 40]
    a: int = 0
    b: int = 5
    assert sub(xs, a, b) == [10, 20, 30, 40]


def test_sub_length_zero() -> None:
    xs: list[int] = []
    a: int = 0
    b: int = 1
    assert sub(xs, a, b) == []


def test_sub_start_outside_list() -> None:
    xs: list[int] = [10, 20, 30]
    a: int = 4
    b: int = 5
    assert sub(xs, a, b) == []


def test_sub_end_zero() -> None:
    xs: list[int] = [10, 20, 30]
    a: int = 0
    b: int = 0
    assert sub(xs, a, b) ==[]
