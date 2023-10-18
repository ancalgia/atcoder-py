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
# 5
# 31 41 59 26 53
# """
# ).strip()


def main():
    (N,), As = IALL(case)

    summary = sum(As)

    As = sorted(As)

    result = 0

    used = 0
    for idx, x in enumerate(As, 1):
        # result += abs((summary - used) - x)
        used += x
        result += abs((x * (N - idx)) - (summary - used))

    print(result)


if __name__ == "__main__":
    main()
