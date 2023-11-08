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
    (N, X), *VPs = IALL(case)

    X = X * 100

    currentAlchohl = 0
    resultCount = 0

    for v, p in VPs:
        resultCount += 1
        currentAlchohl += v * p

        if currentAlchohl > X:
            print(resultCount)
            return

    print(-1)


if __name__ == "__main__":
    main()
