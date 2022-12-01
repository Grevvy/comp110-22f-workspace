"""Tests for linked list utils."""

import pytest
from exercises.ex11.linked_list import Node, last, value_at, max

__author__ = "Your PID"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_non_empty() -> None:
    """Regular use of value_at function."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert value_at(linked_list, 1) == 20


def test_max_non_empty() -> None:
    """Regular use of max function."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert max(linked_list) == 30