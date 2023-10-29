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
# 11 11
# ...#####...
# .##.....##.
# #..##.##..#
# #..##.##..#
# #.........#
# #...###...#
# .#########.
# .#.#.#.#.#.
# ##.#.#.#.##
# ..##.#.##..
# .##..#..##.
#     """
# ).strip()


def createWall(matrix: list[list[str]], H: int, W: int, wall: str) -> list[list[str]]:
    return [[wall] * (W + 2)] + [[wall] + x + [wall] for x in matrix] + [[wall] * (W + 2)]


def isChained(x: int, y: int, matrix: list[list[str]]):
    if any(
        [
            matrix[x - 1][y] == "#",
            matrix[x + 1][y] == "#",
            matrix[x][y - 1] == "#",
            matrix[x][y + 1] == "#",
        ]
    ):
        return True


def main():
    HW, *rest = SL(case)

    H, W = IL(HW)

    matrix = [list(x) for x in rest]

    walled = createWall(matrix, H, W, ".")

    pass

    for x in range(1, H + 1):
        for y in range(1, W + 1):
            if walled[x][y] == "#" and not isChained(x, y, walled):
                print("No")
                return

    print("Yes")


if __name__ == "__main__":
    main()
