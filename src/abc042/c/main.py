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
# 1000 8
# 1 3 4 5 6 7 8 9
#     """
# ).strip()


def main():
    (N, K), Ds = IALL(case)

    dSet = set(map(str, Ds))

    while True:
        hoge = set(str(N)) & dSet
        if len(hoge) == 0:
            print(N)
            return

        N += 1


if __name__ == "__main__":
    main()
