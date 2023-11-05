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
    (N,), Ws, *_ = [list(map(int, x.split())) for x in case.splitlines()]

    ruisekiList: list[int] = []

    summary = 0

    for x in Ws:
        summary += x

        ruisekiList.append(summary)

    smallestAbs = 999999999

    for x in ruisekiList:
        currAbs = abs((ruisekiList[-1] - x) - x)

        if currAbs < smallestAbs:
            smallestAbs = currAbs
        else:
            print(smallestAbs)
            return

    pass


if __name__ == "__main__":
    main()
