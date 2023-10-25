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
    (N,), *ABs = IALL(case)

    aoki = sum([x[0] for x in ABs])
    taka = 0

    sortedABs = sorted(ABs, key=lambda x: x[0] * 2 + x[1], reverse=True)

    result = 0

    for a, b in sortedABs:
        aoki -= a
        taka += a + b
        result += 1

        if taka > aoki:
            print(result)
            return

    pass


if __name__ == "__main__":
    main()
