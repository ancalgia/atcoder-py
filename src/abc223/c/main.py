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
# 3
# 1 3
# 2 2
# 3 1
#     """
# ).strip()
# # 3.83333


def main():
    (N,), *ABs = IALL(case)

    allTIme = sum([a / b for a, b in ABs])

    halfTime = allTIme / 2

    dist = 0

    for a, b in ABs:
        if halfTime > (a / b):
            halfTime -= a / b
            dist += a

        elif halfTime == (a / b):
            dist += a
            break

        else:
            dist += a * (halfTime / (a / b))
            break

    print(dist)


if __name__ == "__main__":
    main()
