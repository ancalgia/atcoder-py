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
# 3 3
# 3 2 2
# 2 1 3
# 1 5 4
#     """
# ).strip()


def createWall(matrix: list[list[int]], H: int, W: int, wall: int) -> list[list[int]]:
    return [[wall] * (W + 2)] + [[wall] + x + [wall] for x in matrix] + [[wall] * (W + 2)]


happy = 0
unhappy = 0


def main():
    (H, W), *martix = IALL(case)

    def check(x: int, y: int, tr: list[int]):
        tr = tr.copy()

        tr.append(walled[x][y])

        if walled[x + 1][y] == 0 and walled[x][y + 1] == 0:
            if len(tr) == len(set(tr)):
                global happy
                happy += 1
            else:
                global unhappy
                unhappy += 1

        if walled[x + 1][y] != 0:
            check(x + 1, y, tr)

        if walled[x][y + 1] != 0:
            check(x, y + 1, tr)

        return

    walled = createWall(martix, H, W, 0)

    # happy = 0
    # unhappy = 0

    currX = 1
    currY = 1

    trace = []

    check(currX, currY, trace)

    print(happy)

    pass


if __name__ == "__main__":
    main()
