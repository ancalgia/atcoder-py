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
    (N,), Ss = IALL(case)

    if len(Ss) == 1:
        print(0)
        return

    diffs = [r - l for l, r in zip(Ss, Ss[1:])]

    boolDiffs = [True if x <= 0 else False for x in diffs]

    maxStep = 0

    currStep = 0

    for x in boolDiffs:
        if x:
            currStep += 1
            maxStep = max([currStep, maxStep])
        else:
            currStep = 0

    print(maxStep)


if __name__ == "__main__":
    main()
