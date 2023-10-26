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


def main():
    (N, K), *ABs = IALL(case)

    friendVilDict: dict[int, int] = dict()

    for a, b in ABs:
        friendVilDict[a] = friendVilDict.get(a, 0) + b

    money = K
    current = 0

    while True:
        if money == 0:
            print(current)
            return

        current += money
        money = 0

        vilKeys = [x for x in friendVilDict if x <= current]

        for key in vilKeys:
            money += friendVilDict[key]
            friendVilDict[key] = 0

    # print(current)


if __name__ == "__main__":
    main()
