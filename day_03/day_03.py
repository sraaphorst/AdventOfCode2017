#!/usr/bin/env python3

# Automatic submission does not appear to be working.
import aocd
import math


def spiral_distance(idx):
    """
    Calculate a distance in a square spiral with 1 at the centre using the Manhattan metric:
    17  16  15  14  13
    18   5   4   3  12
    19   6   1   2  11
    20   7   8   9  10
    21  22  23---> ...
    :param idx: the index number in the spiral
    :return: the distance from the centre of the spiral

    >>> spiral_distance(1)
    0
    >>> list(map(spiral_distance, range(2, 10)))
    [1, 2, 1, 2, 1, 2, 1, 2]
    >>> list(map(spiral_distance, range(10, 26)))
    [3, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4, 3, 2, 3, 4]
    >>> list(map(spiral_distance, range(26, 50)))
    [5, 4, 3, 4, 5, 6, 5, 4, 3, 4, 5, 6, 5, 4, 3, 4, 5, 6, 5, 4, 3, 4, 5, 6]
    """
    sq_odd = lambda x: (2 * x + 1)**2

    # Find the layer that the number is in.
    layer = 0
    while idx > sq_odd(layer):
        layer = layer + 1
    idx = idx - sq_odd(layer - 1)

    # Determine the branch and position of the branch we are in.
    branch = 0 if layer == 0 else (idx - 1) // (2 * layer)
    branch_dists = list(range(layer - 1, 0, -1)) + list(range(layer + 1))
    branch_pos = (idx - 1) % len(branch_dists)

    return layer + branch_dists[branch_pos]


def create_sum_spiral_matrix(radius):
    """
    Create the matrix defined in https://oeis.org/A141481
    :param radius: the radius of the matrix
    :return: the nondescreasing, unrolled spiral

    >>> create_sum_spiral_matrix(5)
    [1, 1, 2, 4, 5, 10, 11, 23, 25, 26, 54, 57, 59, 122, 133, 142, 147, 304, 330, 351, 362, 747, 806, 880, 931]
    """
    assert radius % 2 == 1, "radius must be odd"
    matrix = [[0] * radius for _ in range(radius)]

    # Seed it.
    matrix[radius//2][radius//2] = 1
    unrolled = [1]

    # Calculate the deltas for any given cell for addition. Leave out [0, 0].
    deltas = [(i,j) for i in [-1, 0, 1] for j in [-1, 0, 1] if i != 0 or j != 0]

    # Calculate the directions: we go up, left, down, and right.
    dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    # Now loop, filling in the matrix, by the current radius U L D R.
    curr = (radius // 2, radius // 2)
    for r in range(1, radius//2 + 1):
        # Move down and to the right one to start the next spiral.
        curr = (curr[0] + 1, curr[1] + 1)

        # For 2r, move up, then left, then down, then right
        for d in dirs:
            for _ in range(2 * r):
                # Advance the current position.
                curr = (curr[0] + d[0], curr[1] + d[1])

                # Sum all the deltas around curr in range and then move on.
                positions = [(curr[0] + delta[0], curr[1] + delta[1]) for delta in deltas
                              if delta[0] >= -curr[0] and curr[0] + delta[0] < radius
                              and delta[1] >= -curr[1] and curr[1] + delta[1] < radius]
                matrix[curr[0]][curr[1]] = sum(matrix[pos[0]][pos[1]] for pos in positions)
                unrolled.append(matrix[curr[0]][curr[1]])
    return unrolled


def find_next_largest(num):
    """
    Given a number, crudely find the next largest number in the sum spiral.
    :param num:
    :return: the first number in the spiral > num.

    >>> find_next_largest(57)
    59
    >>> find_next_largest(880)
    931
    """
    radius = 1
    while True:
        spiral = create_sum_spiral_matrix(radius)
        if spiral[-1] > num:
            # Find the first position > num.
            return spiral[next(x[0] for x in enumerate(spiral) if x[1] > num)]
        radius += 2


if __name__ == '__main__':
    session = aocd.get_cookie()
    data = int(aocd.get_data(day=3, year=2017, session=session))

    a1 = spiral_distance(data)
    print("a1 = %r" % a1)
    aocd.submit1(a1, day=1, year=2017, session=session, reopen=False)

    a2 = find_next_largest(data)
    print("a2 = %r" % a2)
    aocd.submit2(a2, day=1, year=2017, session=session, reopen=False)
