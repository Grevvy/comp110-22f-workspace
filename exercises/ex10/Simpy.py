"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730529974"


class Simpy:
    """An object with a list that has many more functions than a simple list."""
    
    values: list[float]

    def __init__(self, values: list[float]):
        """Initializes a simpy."""
        self.values = values

    def __repr__(self) -> str:
        """A representation of a simpy."""
        return f"Simpy({self.values})"
    
    def fill(self, fill_value: float, number_of_values: int) -> None:
        """Fills a simpy with the value specified and the number of times."""
        self.values = []
        for _ in range(0, number_of_values):
            self.values.append(fill_value)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills a simpy with values from a start and stop at a designated interval."""
        assert step != 0.0
        value: float = start
        while value != stop:
            self.values.append(value)
            value += step
    
    def sum(self) -> float:
        """Sums the values in a simpy."""
        return sum(self.values)

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Adds a value to every value in a simpy and also adds two simpys together."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value + rhs)
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] + rhs.values[i])
        return result

    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Raises every value in a simpy to a specified power and also allows for two simpys to be raised to each other."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value ** rhs)
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] ** rhs.values[i])
        return result

    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Determines which values in a simpy are equal to values in another simpy, also if values in a simpy are equal to a specified float value."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                result.append(value == rhs)
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] == rhs.values[i])
        return result

    def __gt__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Determines is values in a simpy are greater than a specified float value. Also determines if one simpy is greater than another simpy."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                result.append(value > rhs)
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] > rhs.values[i])
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Uses a mask to get the values desired in a simpy. Can also be used to retrieve values that match a given argument."""
        result: Simpy = Simpy([])
        if isinstance(rhs, list):
            assert len(self.values) == len(rhs)
            for i in range(len(self.values)):
                if rhs[i] is True:
                    result.values.append(self.values[i])
            return result
        if isinstance(rhs, int):
            return self.values[rhs]