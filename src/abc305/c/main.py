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
# 5 6
# ......
# ..#.#.
# ..###.
# ..###.
# ......
#     """
# ).strip()


def main():
    HW, *rest = SL(case)

    H, W = IL(HW)

    matrix = rest

    rotMatrix = ["".join(x) for x in zip(*rest)]

    left = 5000
    right = -5000

    top = 5000
    bottom = -5000

    for x in matrix:
        if "#" in x:
            left = min([x.find("#"), left])
            right = max([x.rfind("#"), right])

    for x in rotMatrix:
        if "#" in x:
            top = min([x.find("#"), top])
            bottom = max([x.rfind("#"), bottom])

    pass

    for x in range(top, bottom + 1):
        for y in range(left, right + 1):
            if matrix[x][y] == ".":
                print(f"{x+1} {y+1}")
                return


if __name__ == "__main__":
    main()
