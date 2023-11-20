#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


# case: str = "".join([x for x in sys.stdin])

case = "3"

MOD = 10**9 + 7


def main():
    N = int(case)

    if N == 1:
        print(0)
        return

    oneNines = 2

    print((oneNines * (10 ** (N - 2))) % MOD)
    # print((oneNines) % MOD)

    pass


if __name__ == "__main__":
    main()
