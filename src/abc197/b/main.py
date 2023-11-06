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
# 3 5 1 4
# #....
# #####
# ....#
#     """
# ).strip()


def main():
    HWXY, *matrix = SL(case)

    H, W, X, Y = IL(HWXY)

    matrix1: list[list[str]] = list(map(list, matrix))

    tgtLine1 = matrix1[X - 1]
    tgtRight1 = tgtLine1[Y:]
    tgtLeft1 = tgtLine1[: Y - 1][::-1]

    matrix2: list[list[str]] = list(zip(*matrix))

    tgtLine2 = matrix2[Y - 1]
    tgtRight2 = tgtLine2[X:]
    tgtLeft2 = tgtLine2[: X - 1][::-1]

    result = 0

    for x in [tgtRight1, tgtLeft1, tgtRight2, tgtLeft2]:
        for y in x:
            if y == ".":
                result += 1
            else:
                break

    print(result + 1)


if __name__ == "__main__":
    main()
