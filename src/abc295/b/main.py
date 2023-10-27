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
# 4 4
# .1.#
# ###.
# .#2.
# #.##
#     """
# ).strip()


def main():
    def explode(bombX: int, bombY: int, bombLv: int):
        for x in range(R):
            for y in range(C):
                dist = abs(bombX - x) + abs(bombY - y)
                if dist <= bombLv:
                    after[x][y] = "."

    RC, *martix = SL(case)

    R, C = IL(RC)

    before = [list(x) for x in martix]

    after = copy.deepcopy(before)

    for x in range(R):
        for y in range(C):
            here = before[x][y]

            if here not in [".", "#"]:
                explode(x, y, int(here))

    for x in after:
        print("".join(x))


if __name__ == "__main__":
    main()
