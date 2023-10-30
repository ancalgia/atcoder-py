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
# 6 12
# 2 3
# 4 6
# 1 2
# 4 5
# 2 6
# 1 5
# 4 5
# 1 3
# 1 2
# 2 6
# 2 3
# 2 5
# 5
# 3 5
# 1 4
# 2 6
# 4 6
# 5 6
#     """
# ).strip()


def main():
    (N, M), *rest = IALL(case)

    ABs = [x for x in rest[:M]]

    CDs = [x for x in rest[M + 1 :]]

    allPtn = itertools.product(*CDs)

    result = 0

    for x in allPtn:
        setX = set(x)

        tmp = len([a for a, b in ABs if a in setX and b in setX])

        if result < tmp:
            result = tmp

    print(result)


if __name__ == "__main__":
    main()
