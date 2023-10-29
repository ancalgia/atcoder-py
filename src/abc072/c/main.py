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
# 10
# 0 0 0 0 0 0 0 0 0 0
#     """
# ).strip()


def main():
    (N,), As = IALL(case)

    if N == 1:
        print(1)
        return

    As.sort()

    maxA = max(As)

    result = 0

    for x in range(maxA + 1):
        le = bisect.bisect_left(As, x)
        # ri = bisect.bisect_left(As, x + 2)
        ri = bisect.bisect_right(As, x + 2)

        result = max([result, ri - le])

    print(result)


if __name__ == "__main__":
    main()
