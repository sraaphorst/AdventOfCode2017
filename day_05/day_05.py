#!/usr/bin/env python3

# Automatic submission does not appear to be working.
import aocd


def calculate_escape(instructions):
    """
    Determine the number of instruction jumps that a program needs to escape its source code.
    Every time a jump is reached, it is incremented by 1.
    :param instructions: a list of the instructions as integers
    :return: the number of jumps it takes to escape the instructions

    >>> calculate_escape([0, 3, 0, 1, -3])
    5
    """
    instructionsp = instructions[:]
    pos = 0
    ctr = 0
    while 0 <= pos < len(instructionsp):
        instructionsp[pos], pos = instructionsp[pos] + 1, pos + instructionsp[pos]
        ctr = ctr + 1
    return ctr


def calculate_escape2(instructions):
    """
    Determine the number of instruction jumps that a program needs to escape its source code.
    Every time a jump is reached, if less than 3, it is incremented by 1; otherwise, it is decremented by 1.
    :param instructions: a list of the instructions as integers
    :return: the number of jumps it takes to escape the instructions

    >>> calculate_escape2([0, 3, 0, 1, -3])
    10
    """
    instructionsp = instructions[:]
    pos = 0
    ctr = 0
    while 0 <= pos < len(instructionsp):
        instructionsp[pos], pos = instructionsp[pos] + (1 if instructionsp[pos] < 3 else - 1), pos + instructionsp[pos]
        ctr = ctr + 1
    return ctr


if __name__ == '__main__':
    session = aocd.get_cookie()
    data = aocd.get_data(day=5, year=2017, session=session)
    instructions = list(map(int, data.split()))

    a1 = calculate_escape(instructions)
    print("a1 = %r" % a1)
    aocd.submit1(a1, day=1, year=2017, session=session, reopen=False)

    a2 = calculate_escape2(instructions)
    print("a2 = %r" % a2)
    aocd.submit2(a1, day=1, year=2017, session=session, reopen=False)
