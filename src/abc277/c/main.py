#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])

# from textwrap import dedent

# case = dedent(
#     """
# 6
# 1 3
# 1 5
# 1 12
# 3 5
# 3 12
# 5 12
#     """
# ).strip()


def main():
    (N,), *ABs = IALL(case)

    upDict: dict[int, set[int]] = dict()
    downDict: dict[int, set[int]] = dict()

    for ab in ABs:
        ab.sort()

        if ab[0] not in upDict:
            upDict[ab[0]] = {ab[1]}
        else:
            upDict[ab[0]].add(ab[1])

        if ab[1] not in downDict:
            downDict[ab[1]] = {ab[0]}
        else:
            downDict[ab[1]].add(ab[0])

    currentAble = {1}

    while True:
        tmpLen = len(currentAble)

        newAble: set[int] = set()
        for x in currentAble:
            if x in upDict:
                newAble.update(upDict[x])
                upDict.pop(x)
            if x in downDict:
                newAble.update(downDict[x])
                downDict.pop(x)

        currentAble.update(newAble)

        if len(currentAble) == tmpLen:
            print(max(currentAble))
            return

    pass


if __name__ == "__main__":
    main()
