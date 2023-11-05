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
# 8 1
# 8 1
#     """
# ).strip()


def main():
    H, W, R, C = IL(case)

    if H == W == 1:
        print(0)
        return

    if H == 1:
        A = 0
    else:
        A = 1 if R in [1, H] else 2

    if W == 1:
        B = 0
    else:
        B = 1 if C in [1, W] else 2

    print(A + B)


if __name__ == "__main__":
    main()
