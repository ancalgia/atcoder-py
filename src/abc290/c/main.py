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
# 7 3
# 2 0 2 3 2 1 9
#     """
# ).strip()


def main():
    (N, K), As = IALL(case)

    AsSet = set(As)

    for x in range(K):
        if x not in AsSet:
            print(x)
            return

    print(K)


if __name__ == "__main__":
    main()
