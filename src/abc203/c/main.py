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
# 3 2
# 5 5
# 2 1
# 2 2
#     """
# ).strip()
# # 10


def main():
    (N, K), *ABs = IALL(case)

    # friendVilDict: dict[int, int] = dict()

    # for a, b in ABs:
    #     friendVilDict[a] = friendVilDict.get(a, 0) + b

    ABs.sort()

    Akeys = [x[0] for x in ABs]

    money = K
    current = 0

    while True:
        if money == 0:
            print(current)
            return

        le = bisect.bisect_right(Akeys, current)
        ri = bisect.bisect_right(Akeys, current + money)

        earns = [x[1] for x in ABs[le:ri]]

        current += money
        money = sum(earns)


if __name__ == "__main__":
    main()
