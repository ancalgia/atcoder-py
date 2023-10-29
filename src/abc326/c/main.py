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
# 10 1
# 3 1 4 1 5 9 2 6 5 3
#     """
# ).strip()


def main():
    (N, M), As = IALL(case)

    As.sort()

    result = 0

    for i, x in enumerate(As):
        left = bisect.bisect_left(As, x)
        rightIdx = bisect.bisect_left(As, x + M - 0.5)

        tmp = rightIdx - left

        result = max([result, tmp])

    print(result)


if __name__ == "__main__":
    main()
