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
# 3 9 5
# 4 8 5
# 5 7 5
#     """
# ).strip()


def main():
    (N,), *APXs = IALL(case)

    lowest = 999999999999

    for a, p, x in APXs:
        available = a < x

        if available:
            lowest = min([lowest, p])

    if lowest == 999999999999:
        print(-1)
        return

    else:
        print(lowest)

    pass


if __name__ == "__main__":
    main()
