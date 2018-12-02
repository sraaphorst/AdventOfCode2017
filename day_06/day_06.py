#!/usr/bin/env python3

# Automatic submission does not appear to be working.
import aocd


def redistribution_count(banks):
    """
    Memory banks are reallocated: iteratively find the bank with the most blocks, and then, starting with the bank
    after that bank (and looping around), redistribute the blocks. Continue until reaching an already-seen state.
    :param banks: the memory banks, represented by a list with the number of blocks each contains
    :return: the index where we discover an infinite loop will occur, and the number of cycles in the loop

    >>> redistribution_count([0, 2, 7, 0])
    (5, 4)
    """
    currbanks = banks[:]
    previous_banks = []
    lenbanks = len(banks)

    while currbanks not in previous_banks:
        previous_banks.append(currbanks[:])

        # Find the index of the largest element.
        index = currbanks.index(max(currbanks))

        redistribution, currbanks[index] = currbanks[index], 0
        for _ in range(redistribution):
            index = (index + 1) % lenbanks
            currbanks[index] = currbanks[index] + 1

    return len(previous_banks), len(previous_banks) - previous_banks.index(currbanks)


if __name__ == '__main__':
    session = aocd.get_cookie()
    data = aocd.get_data(day=6, year=2017, session=session)
    banks = list(map(int, data.split()))

    a1, a2 = redistribution_count(banks)
    print("a1 = %r" % a1)
    aocd.submit1(a1, day=1, year=2017, session=session, reopen=False)
    print("a2 = %r" % a2)
    aocd.submit2(a1, day=1, year=2017, session=session, reopen=False)
