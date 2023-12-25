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
# 5 1000000000
# 583563238 820642330 44577
# 136809000 653199778 90962
# 54601291 785892285 50554
# 5797762 453599267 65697
# 468677897 916692569 87409    """
# ).strip()


def main():
    (N, C), *ABCs = IALL(case)

    cumDict: dict[int, int] = {}

    for a, b, c in ABCs:
        if (a - 1) in cumDict:
            cumDict[a - 1] += c
        else:
            cumDict[a - 1] = c
        if b in cumDict:
            cumDict[b] -= c
        else:
            cumDict[b] = -c

    cumDictList = sorted(list(cumDict.items()))

    tmp = 0
    result = 0

    exDay = 0

    for day, price in cumDictList:
        result += min(tmp, C) * (day - exDay)

        exDay = day
        tmp += price

    print(result)


if __name__ == "__main__":
    main()
