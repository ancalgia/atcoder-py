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
# 4 10
# 1 3 5
# 2 4 4
# 3 10 6
# 2 3 1
#     """
# ).strip()


def main():
    (N, W), *STPs = IALL(case)

    cum = [0 for x in range((10**5 * 2) + 100)]

    for s, t, p in STPs:
        cum[s] += p
        cum[t] -= p

    tmp = 0

    for x in cum:
        tmp += x

        if tmp > W:
            print("No")
            return

    print("Yes")


if __name__ == "__main__":
    main()
