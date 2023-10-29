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
# 4
# 6 13 12 5 3 7 10 11 16 9 8 15 2 1 14 4
#     """
# ).strip()


def main():
    (N,), As = IALL(case)

    left = max(As[: 2 ** (N - 1)])
    right = max(As[2 ** (N - 1) :])

    key = min([left, right])
    print(As.index(key) + 1)


if __name__ == "__main__":
    main()
