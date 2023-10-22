#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on

import sys

sys.setrecursionlimit(100000)


case: str = "".join([x for x in sys.stdin])


# from textwrap import dedent

# case = dedent(
#     """
# 5 6
# .##...
# ...#..
# ....##
# #.#...
# ..#...
#     """
# ).strip()


matrix: list[list[str]] = []


def main():
    HW, *rest = SL(case)

    H, W = map(int, HW.split())

    global matrix

    matrix = [list(x) for x in rest]

    matrix = [list("." + x + ".") for x in rest]

    matrix = [list("." * (W + 2))] + matrix + [list("." * (W + 2))]

    count = 0

    for x in range(H):
        for y in range(W):
            if matrix[x][y] == "#":
                matrix[x][y] = "."
                check(x, y)
                count += 1

    print(count)

    pass


def check(x: int, y: int):
    pass

    global matrix

    if matrix[x - 1][y - 1] == "#":
        matrix[x - 1][y - 1] = "."
        check(x - 1, y - 1)
    if matrix[x - 1][y] == "#":
        matrix[x - 1][y] = "."
        check(x - 1, y)
    if matrix[x - 1][y + 1] == "#":
        matrix[x - 1][y + 1] = "."
        check(x - 1, y + 1)

    if matrix[x][y - 1] == "#":
        matrix[x][y - 1] = "."
        check(x, y - 1)

    if matrix[x][y + 1] == "#":
        matrix[x][y + 1] = "."
        check(x, y + 1)

    if matrix[x + 1][y - 1] == "#":
        matrix[x + 1][y - 1] = "."
        check(x + 1, y - 1)
    if matrix[x + 1][y] == "#":
        matrix[x + 1][y] = "."
        check(x + 1, y)
    if matrix[x + 1][y + 1] == "#":
        matrix[x + 1][y + 1] = "."
        check(x + 1, y + 1)


if __name__ == "__main__":
    main()
