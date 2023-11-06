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
# 5 3 6 8
# -10 3 1 5 -100
# 100 6 14
#     """
# ).strip()
# #  W


# 3 2 10 20
# 8 15 13
# 16 22

# expected:
# No_War


def main():
    (N, M, X, Y), Xs, Ys = IALL(case)

    XRight = max(Xs + [X])
    YLeft = min(Ys + [Y])

    if X >= YLeft or Y <= XRight:
        print("War")
        return

    print("War") if XRight >= YLeft else print("No War")


if __name__ == "__main__":
    main()
