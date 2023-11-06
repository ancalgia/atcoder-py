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
    A, B, C, D = IL(case)

    # isNegative1 = B < 0
    # isNegative2 = D < 0

    allPattern = itertools.product([A, B], [C, D])

    results = []

    for le, ri in allPattern:
        results.append(le * ri)

    print(max(results))


if __name__ == "__main__":
    main()
