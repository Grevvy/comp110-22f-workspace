"""List utility functions."""

__author__ = "730529974"


def all(numbers: list[int], compared_number: int) -> bool:
    """Determines if all the numbers in a list are equal to a number."""
    i = 0
    run_end: bool = False
    assert len(numbers) >= 1
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
    if len(numbers) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 1
    a: int = 0
    biggest: list[int] = list()
    biggest.append(numbers[0])
    while i < len(numbers):
        if numbers[i] > biggest[a]:
            biggest.append(numbers[i])
        else:
            biggest.append(biggest[a])
        i += 1
        a += 1
    return biggest.pop(len(biggest) - 1)


def is_equal(input_one: list[int], input_two: list[int]) -> bool:
    """Determines if every integer in a list is equal to each element in another list."""
    i: int = 0
    a: int = 0
    b: int = 0
    c: int = 0
    run_end: bool = False
    run_end_two: bool = False
    while i < len(input_one):
        while a < len(input_two) and run_end is False:
            if input_one[i] == input_two[a]:
                run_end = False
            else:
                run_end = True
            a += 1
        i += 1
    while b < len(input_two):
        while c < len(input_one) and run_end_two is False:
            if input_two[b] == input_one[c]:
                run_end = False
            else:
                run_end = True
            c += 1
        b += 1
    if run_end or run_end_two is True:
        return False
    else:
        return True


def main() -> None:
    """Testing for the list utility functions."""
    print(is_equal([1, 1, 0], [1, 0, 1]))


if __name__ == "__main__":
    main()