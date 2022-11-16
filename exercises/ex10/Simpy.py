"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730529974"


class Simpy:
    values: list[float]

    def __init__(self, values: list[float]):
        self.values = values

    def __repr__(self) -> str:
        return f"Simpy({self.values})"
    
    def fill(self, fill_value: float, number_of_values: int):
        self.values = []
        for _ in range(0, number_of_values):
            self.values.append(fill_value)

    def arange(self, start: float, stop: float, step: float = 1.0):
        assert step != 0.0
        value: float = start
        while value != stop:
            self.values.append(value)
            value += step
    
    def sum(self) -> float:
        return sum(self.values)

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
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
        result: Simpy = Simpy([])
        if isinstance(rhs, list):
            assert len(self.values) == len(rhs)
            for i in range(len(self.values)):
                if rhs[i] == True:
                    result.values.append(self.values[i])
            return result
        if isinstance(rhs, int):
            return self.values[rhs]
        


