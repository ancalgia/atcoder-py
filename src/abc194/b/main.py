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

    # 一人の場合の最短時間
    singleMin = min([x[0] + x[1] for x in ABs])

    # 二人の場合(全探索)
    allComb = itertools.combinations(ABs, 2)

    doubleMin = 99999999999

    for a, b in allComb:
        tmp = min([max([a[0], b[1]]), max([a[1], b[0]])])

        doubleMin = min([doubleMin, tmp])

    print(min([singleMin, doubleMin]))


if __name__ == "__main__":
    main()
