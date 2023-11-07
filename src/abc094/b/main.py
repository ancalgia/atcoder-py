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
    (N, M, X), As = IALL(case)

    As = set(As)

    foreResult = 0

    for x in range(X, N):
        if x in As:
            foreResult += 1

    backResult = 0

    for x in range(X, 0, -1):
        if x in As:
            backResult += 1

    print(min([foreResult, backResult]))


if __name__ == "__main__":
    main()
