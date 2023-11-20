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


case: str = "".join([x for x in sys.stdin])

# from textwrap import dedent

# case = dedent(
#     """
# 5 9
# #.#.#...#
# .#...#.#.
# #.#...#..
# .....#.#.
# ....#...#
#     """
# ).strip()


def main():
    HW, *matrix = SL(case)

    H, W = IL(HW)

    matrix = [list(x) for x in matrix]

    walled = createWall(matrix, H, W, "/")

    minHW = min(H, W)

    results = [0 for x in range(minHW)]

    for x in range(1, H + 1):
        for y in range(1, W + 1):
            if walled[x][y] == "#":
                if all(
                    [
                        walled[x + 1][y + 1] == "#",
                        walled[x + 1][y - 1] == "#",
                        walled[x - 1][y + 1] == "#",
                        walled[x - 1][y - 1] == "#",
                    ],
                ):
                    tmp = 1
                    while True:
                        if walled[x + tmp + 1][y + tmp + 1] == "#":
                            tmp += 1

                        else:
                            results[tmp - 1] += 1
                            break

    print(*results)


if __name__ == "__main__":
    main()
