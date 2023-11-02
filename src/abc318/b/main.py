#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


# from textwrap import dedent

# case = dedent(
#     """
# 3
# 0 5 1 3
# 1 4 0 5
# 2 5 2 4
#     """
# ).strip()

# 3
# 0 5 1 3


def main():
    (N,), *ABCDs = IALL(case)

    matrix = [[0 for y in range(101)] for x in range(101)]

    for a, b, c, d in ABCDs:
        matrix[a][c] += 1
        matrix[a][d] -= 1
        matrix[b][c] -= 1
        matrix[b][d] += 1

    matrix2 = [[0 for y in range(101)] for x in range(101)]

    for x in range(101):
        tmp = 0
        for y in range(101):
            tmp += matrix[x][y]
            matrix2[x][y] = tmp

    matrix2: list[list[int]] = list(map(list, zip(*matrix2)))

    for x in range(101):
        last = 0
        for y in range(101):
            matrix2[x][y] += last
            last = matrix2[x][y]

    result = 0

    for x in matrix2:
        result += len([z for z in x if z >= 1])

    print(result)


if __name__ == "__main__":
    main()
