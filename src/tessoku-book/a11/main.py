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
# 15 47
# 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67
#     """
# ).strip()


def main():
    (N, X), As = IALL(case)

    AsWithIndex = [[x, idx] for idx, x in enumerate(As)]

    while True:
        if len(AsWithIndex) == 1:
            print(AsWithIndex[0][1] + 1)
            return

        separator = int(len(AsWithIndex) / 2)

        if AsWithIndex[separator][0] > X:
            AsWithIndex = AsWithIndex[:separator]
        else:
            AsWithIndex = AsWithIndex[separator:]


if __name__ == "__main__":
    main()
