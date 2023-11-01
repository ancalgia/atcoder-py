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
    (N,), *XYs = IALL(case)

    allSet = itertools.combinations(XYs, 2)

    result = 0
    for a, b in allSet:
        if abs(b[1] - a[1]) == 0:
            result += 1
            continue

        if abs(b[0] - a[0]) / abs(b[1] - a[1]) >= 1:
            result += 1
            continue

    print(result)


if __name__ == "__main__":
    main()
