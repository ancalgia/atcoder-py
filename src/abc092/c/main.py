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
    (N,), As = IALL(case)

    As = [0] + As + [0]

    allDiffs = [abs(right - left) for left, right in zip(As, As[1:])]

    allDiffSum = sum(allDiffs)

    for x in range(N):
        del1 = allDiffs[x]
        del2 = allDiffs[x + 1]

        add1 = abs(As[x] - As[x + 2])

        print(allDiffSum - del1 - del2 + add1)


if __name__ == "__main__":
    main()
