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
    (N, X), *ABs = IALL(case)

    ableSet: set[int] = set({0})

    for a, b in ABs:
        tmpSet: set[int] = set()

        for x in ableSet:
            tmpSet.add(x + a)
            tmpSet.add(x + b)

        ableSet = tmpSet

    print("Yes") if X in ableSet else print("No")


if __name__ == "__main__":
    main()
