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
# 31 3
# 20 8
# 11 5
# 4 3
# 47 14
# 1 18
#     """
# ).strip()

# # 67


def main():
    (N,), *WXs = IALL(case)

    sortedWXs = sorted(WXs, key=lambda x: x[1])

    tomorrowsortedWXs = [[x[0], x[1] + 24] for x in sortedWXs]

    doubleSortedWXs = sortedWXs + tomorrowsortedWXs

    doubleDict: dict[int, int] = dict()

    for x in doubleSortedWXs:
        if x[1] in doubleDict:
            doubleDict[x[1]] += x[0]
        else:
            doubleDict[x[1]] = x[0]

    maxMembers = 0

    for x in range(23):
        # frm = x

        # until = x + 9

        currentMember = sum([doubleDict.get(y, 0) for y in range(x, x + 9)])

        maxMembers = max([maxMembers, currentMember])

    print(maxMembers)


if __name__ == "__main__":
    main()
