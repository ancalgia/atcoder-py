#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


def main():
    (N,), (T, A), Hs = IALL(case)

    minDiff = 999999999999999999999999
    result = 0

    for idx, h in enumerate(Hs, 1):
        tmpKion = T - (h * 0.006)

        tmpDiff = abs(A - tmpKion)

        if minDiff > tmpDiff:
            minDiff = tmpDiff
            result = idx

    print(result)


if __name__ == "__main__":
    main()
