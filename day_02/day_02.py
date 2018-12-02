#!/usr/bin/env python3

# Automatic submission does not appear to be working.
import aocd
import itertools


def calc_biggest_row_difference(row):
    """
    Calculate the biggest difference between two elements in the row.
    :param row: the row data
    :return: the difference between the largest and smallest element

    >>> calc_biggest_row_difference("5 1 9 5")
    8
    >>> calc_biggest_row_difference("7 5 3")
    4
    >>> calc_biggest_row_difference("2 4 6 8")
    6
    """
    rowint = list(map(int, row.split()))
    return max(rowint) - min(rowint)


def calc_biggest_row_sum(rows):
    """
    Calculate the sum of the biggest differences across the rows
    :param rows: block string comprising row data
    :return: the sum of the largest row differences

    >>> calc_biggest_row_sum('5 1 9 5\\n7 5 3\\n2 4 6 8')
    18
    """
    return sum(map(calc_biggest_row_difference, rows.split('\n')))


def calc_row_division(row):
    """
    Calculate the only division between two numbers in the row where one divides the other
    :param row: the row data
    :return: the result of the division of the two numbers

    >>> calc_row_division('5 9 2 8')
    4
    >>> calc_row_division('9 4 7 3')
    3
    >>> calc_row_division('3 8 6 5')
    2
    """
    rowint = list(map(int, row.split()))
    divisions = [i[0] // i[1] + i[1] // i[0] for i in itertools.combinations(rowint, 2)
                 if i[0] % i[1] == 0 or i[1] % i[0] == 0]
    if len(divisions) != 1:
        raise ValueError("illegal row: " + row)
    return divisions[0]


def calc_row_division_sum(rows):
    """
    Calculate the sum of the row divisions
    :param rows: block string comprising the row data
    :return: the sum of the only divisible elements per row

    >>> calc_row_division_sum('5 9 2 8\\n9 4 7 3\\n3 8 6 5')
    9
    """
    return sum(map(calc_row_division, rows.split('\n')))


if __name__ == '__main__':
    session = aocd.get_cookie()
    data = aocd.get_data(day=2, year=2017, session=session)

    a1 = calc_biggest_row_sum(data)
    print("a1 = %r" % a1)
    aocd.submit1(a1, day=1, year=2017, session=session, reopen=False)

    a2 = calc_row_division_sum(data)
    print("a2 = %r" % a2)
    aocd.submit2(a2, day=1, year=2017, session=session, reopen=False)
