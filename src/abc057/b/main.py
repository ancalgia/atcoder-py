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
    (N, M), *rest = IALL(case)

    ABs = rest[:N]
    CDs = rest[N:]

    result: list[int] = []

    for a, b in ABs:
        minDist = 99999999999999
        minIdx = 0

        for idx, (c, d) in enumerate(CDs):
            dist = abs(a - c) + abs(b - d)

            if dist < minDist:
                minDist = dist
                minIdx = idx + 1

        result.append(minIdx)

    [print(x) for x in result]


if __name__ == "__main__":
    main()
