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
    (N, K), As, *XYs = IALL(case)

    farestDist = 0

    lighters = [x for idx, x in enumerate(XYs, 1) if idx in As]

    for idx, (x, y) in enumerate(XYs, 1):
        if idx in As:
            continue

        nearest = 999999999999
        for lx, ly in lighters:
            tmpDist = math.sqrt((lx - x) ** 2 + (ly - y) ** 2)
            nearest = min([tmpDist, nearest])

        farestDist = max([farestDist, nearest])

    print(farestDist)


if __name__ == "__main__":
    main()
