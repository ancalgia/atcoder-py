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
# 10 4
# 1346 1347 1348 1349
#     """
# ).strip()


def main():
    (N, M), *matrix = IALL(case)

    firstLine = matrix[0]

    firstCell = firstLine[0] % 7

    if firstCell not in [0, 6, 5, 4, 3, 2, 1][M - 1 :]:
        print("No")
        return

    for x in matrix:
        a = [right - left for left, right in zip(x, x[1:])]

        if any([z != 1 for z in a]):
            print("No")
            return

    for x in zip(*matrix):
        a = [right - left for left, right in zip(x, x[1:])]
        if any([z != 7 for z in a]):
            print("No")
            return
        else:
            print("Yes")
            return


if __name__ == "__main__":
    main()
