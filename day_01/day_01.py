#!/usr/bin/env python3

# Automatic submission does not appear to be working.
import aocd


def find_paired_elements(lst):
    """
    Scan the list and find digits where the previous digit matched.
    :param lst: the data list
    :return: the list of data where the previous element matched.

    >>> sum(find_paired_elements("1122"))
    3
    >>> sum(find_paired_elements("1111"))
    4
    >>> sum(find_paired_elements("1234"))
    0
    >>> sum(find_paired_elements("91212129"))
    9
    """
    return [int(lst[i]) for i in range(len(lst)) if lst[i] == lst[i-1]]


def find_cyclically_paired_elements(lst):
    """
    Scan the list and find data from the first half that is paired with data in the second half by going
    halfway around the list.
    :param lst: the data list
    :return: the list of data from the first half that pairs with the second half

    >>> 2 * sum(find_cyclically_paired_elements("1212"))
    6
    >>> 2 * sum(find_cyclically_paired_elements("1221"))
    0
    >>> 2 * sum(find_cyclically_paired_elements("123425"))
    4
    >>> 2 * sum(find_cyclically_paired_elements("123123"))
    12
    >>> 2 * sum(find_cyclically_paired_elements("12131415"))
    4
    """
    return [int(lst[i]) for i in range(len(lst)//2) if lst[i] == lst[len(lst)//2+i]]


if __name__ == '__main__':
    session = aocd.get_cookie()
    data = aocd.get_data(day=1, year=2017, session=session)

    a1 = sum(find_paired_elements(data))
    print("a1 = %r" % a1)
    aocd.submit1(a1, day=1, year=2017, session=session, reopen=False)

    a2 = 2 * sum(find_cyclically_paired_elements(data))
    print("a2 = %r" % a2)
    aocd.submit2(a1, day=1, year=2017, session=session, reopen=False)
