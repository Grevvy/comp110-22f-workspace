"""List utility functions."""

__author__ = "730529974"

def all(numbers: list[int], compared_number: int) -> bool:
    """Determines if all the numbers in a list are equal to a number."""
    i = 0
    run_end: bool = False
    while i < len(numbers) and run_end is False:
        if numbers[i] == compared_number:
            run_end = False
        else:
            run_end = True
        i += 1
    if run_end is False:
        return True
    else:
        return False

def max(numbers: list[int]) -> int:
    """Determines the largest number in a list."""
    i = 0
    biggest: int = 0
    if len(numbers) == 0:
        raise ValueError("max() arg is an empty List")
    while i < len(numbers) and biggest <= numbers[i]:
        if numbers[i] > numbers[i + 1]:
            biggest = numbers[i]
        else:
            biggest = numbers[i + 1]
        i += 1
    return biggest

def is_equal(input_one: list[int], input_two: list[int]) -> bool:
    """Determines if every integer in a list is equal to each element in another list."""
    i: int = 0
    run_end: bool = False
    while i < len(input_one) and run_end is False:
        if input_one[i] == input_two[i]:
            run_end = False
        else:
            run_end = True
        i += 1
    if run_end is True:
        return False
    else:
        return True


def main() -> None:
    """Testing for the list utility functions."""
    print(is_equal([1, 0, 1], [1, 0, 1]))

if __name__ == "__main__":
    main()