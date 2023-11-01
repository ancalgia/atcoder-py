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
# 8 1 3 5 7
# 1 2 3 4 5 6 7 8
#     """
# ).strip()


# output:
# [1,_6,_7,_8,_4,_5,_2,_3,_4,_8]


def main():
    (N, P, Q, R, S), As = IALL(case)

    PQ = As[P - 1 : Q]
    RS = As[R - 1 : S]

    result = As[: P - 1] + RS + As[Q : R - 1] + PQ + As[S:]

    print(*result)


if __name__ == "__main__":
    main()
