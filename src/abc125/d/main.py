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
# 5
# 10 -4 -8 -11 3
#     """
# ).strip()


def main():
    (N,), As = IALL(case)

    allsPositiveSum = sum(list(map(abs, As)))

    # if N % 2 == 1:
    #     print(allsPositiveSum)
    #     return

    minusCount = len([x for x in As if x < 0])

    if minusCount % 2 == 1:
        absMin = min(list(map(abs, As)))
        print(allsPositiveSum - (absMin * 2))

    else:
        print(allsPositiveSum)


if __name__ == "__main__":
    main()
