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
    (N, X), Xs = IALL(case)

    if len(Xs) == 1:
        print(abs(X - Xs[0]))
        return

    sortedXs = sorted(Xs)

    WithStart = sorted(sortedXs + [X])

    diffsWithStart = [r - l for l, r in zip(WithStart, WithStart[1:])]

    minDiff2 = min(diffsWithStart)

    # hoge = bisect.bisect_left(sortedXs, X)

    # minDistance = min([abs(city - X) for city in sortedXs])

    diffsWithStartSet = set(diffsWithStart)

    for x in range(minDiff2, 0, -1):
        isOk = True
        for y in diffsWithStartSet:
            if y % x != 0:
                isOk = False
                break

        if isOk:
            print(x)
            return

    pass


if __name__ == "__main__":
    main()
