#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys

import numpy


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])

# from textwrap import dedent

# case = dedent(
#     """
# 3 4
# ##.#
# ##..
# #...
# .###
# ..##
# ...#
#     """
# ).strip()
# case = dedent(
#     """
# 8 7
# #..#..#
# .##.##.
# #..#..#
# .##.##.
# #..#..#
# .##.##.
# #..#..#
# .##.##.
# ....###
# ####...
# ....###
# ####...
# ....###
# ####...
# ....###
# ####...
#     """
# ).strip()


def main():
    HW, *rest = SL(case)

    H, W = map(int, HW.split())

    S = [x for x in rest[:H]]
    T = [x for x in rest[H : H + H]]
    # S = [sorted(x) for x in rest[:H]]
    # T = [sorted(x) for x in rest[H : H + H]]

    # *でばらしてzipで固めると軸交換したことになるもよう。。。
    S = sorted(["".join(x) for x in zip(*S)])
    T = sorted(["".join(x) for x in zip(*T)])

    # for a, b in zip(sorted(S), sorted(T)):
    for a, b in zip(S, T):
        if (a) != (b):
            print("No")
            return

    print("Yes")
    return


if __name__ == "__main__":
    main()
