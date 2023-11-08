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
    (H, W, N), *ABs = IALL(case)

    ABs = [[x[0], x[1], idx] for idx, x in enumerate(ABs)]

    ABs.sort()

    lastA = 0
    lastNum = 0
    for x in ABs:
        if x[0] != lastA:
            lastNum += 1
            lastA = x[0]

        x[0] = lastNum

    ABs.sort(key=lambda x: x[1])

    lastA = 0
    lastNum = 0
    for x in ABs:
        if x[1] != lastA:
            lastNum += 1
            lastA = x[1]

        x[1] = lastNum

    ABs.sort(key=lambda x: x[2])

    [print(f"{x[0]} {x[1]}") for x in ABs]


if __name__ == "__main__":
    main()
