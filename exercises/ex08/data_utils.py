"""Dictionary related utility functions."""

__author__ = "730529974"

# Define your functions below


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(table: dict[str, list[str]], number_of_rows: int) -> dict[str, list[str]]:
    """Only returns the number of rows specified."""
    result: dict[str, list[str]] = {}
    for column in table:
        i: int = 0
        values: list[str] = []
        while i < number_of_rows and i < len(table[column]):
            values.append(table[column][i])
            i += 1
        result[column] = values
    return result


def select(col_table: dict[str, list[str]], col_names: list[str]) -> dict[str, list[str]]:
    """Returns the desired columns by name."""
    result: dict[str, list[str]] = {}
    for column in col_table:
        if column in col_names:
            result[column] = col_table[column]
    return result


def concat(first_table: dict[str, list[str]], second_table: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two tables into one table."""
    result: dict[str, list[str]] = {}
    for column in first_table:
        result[column] = first_table[column]
    for column in second_table:
        if column in result:
            result[column] += second_table[column]
        else:
            result[column] = second_table[column]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Counts the number of times a value occurs."""
    result: dict[str, int] = {}
    for i in values:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result    