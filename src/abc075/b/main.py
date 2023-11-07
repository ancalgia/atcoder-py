#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


def createWall(matrix: list[list[str]], H: int, W: int, wall: str) -> list[list[str]]:
    return [[wall] * (W + 2)] + [[wall] + x + [wall] for x in matrix] + [[wall] * (W + 2)]


def removeWall(matrix: list[list[str]]) -> list[list[str]]:
    return [x[1:-1] for x in matrix[1:-1]]


def CountMine(x: int, y: int, matrix: list[list[str]]):
    return [
        matrix[x - 1][y] == "#",
        matrix[x + 1][y] == "#",
        matrix[x][y - 1] == "#",
        matrix[x][y + 1] == "#",
        matrix[x + 1][y + 1] == "#",
        matrix[x + 1][y - 1] == "#",
        matrix[x - 1][y + 1] == "#",
        matrix[x - 1][y - 1] == "#",
    ].count(True)


case: str = "".join([x for x in sys.stdin])


def main():
    HW, *matrix = SL(case)
    H, W = IL(HW)

    matrix = [list(x) for x in matrix]

    matrix = createWall(matrix, H, W, "@")

    for x in range(1, H + 1):
        for y in range(1, W + 1):
            if matrix[x][y] == ".":
                matrix[x][y] = str(CountMine(x, y, matrix))

    matrix = removeWall(matrix)
    [print("".join(x)) for x in matrix]

    pass


if __name__ == "__main__":
    main()
