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
# 5 7
#     """
# ).strip()


def main():
    (K,), (A, B) = IALL(case)

    condition = (A % K == 0 or B % K == 0) or B // K != A // K

    print("OK") if condition else print("NG")


if __name__ == "__main__":
    main()
