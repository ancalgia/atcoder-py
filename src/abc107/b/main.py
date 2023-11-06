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
# ##.#
# ....
# ##.#
# .#.#
#     """
# ).strip()


def main():
    NW, *matrix = SL(case)

    matrix2 = [x for x in matrix if "#" in x]

    rotated = list(zip(*matrix2))

    matrix3 = [x for x in rotated if "#" in x]

    rotated2 = list(zip(*matrix3))

    for x in rotated2:
        print("".join(x))


if __name__ == "__main__":
    main()
