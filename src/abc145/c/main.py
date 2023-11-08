#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


def getDistance(le: tuple[int, int], ri: tuple[int, int]) -> float:
    dist = math.sqrt((le[0] - ri[0]) ** 2 + (le[1] - ri[1]) ** 2)
    return dist


case: str = "".join([x for x in sys.stdin])


def main():
    (N,), *XYs = IALL(case)

    XYs = [(x, y) for x, y in XYs]

    allPtn = itertools.permutations(XYs)

    distList: list[float] = []

    for ptn in allPtn:
        tmpDist = sum([getDistance(left, right) for left, right in zip(ptn, ptn[1:])])

        distList.append(tmpDist)

    print(sum(distList) / len(distList))


if __name__ == "__main__":
    main()
