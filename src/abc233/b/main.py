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
# 3 7
# abcdefgh
#     """
# ).strip()


# # expected:
# # meramtsirhcyrs


def main():
    LR, S = SL(case)

    L, R = IL(LR)

    S = S[: L - 1] + S[L - 1 : R][::-1] + S[R:]

    print(S)


if __name__ == "__main__":
    main()
