#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])

# case = "6 2 3 3"  # 1


# case = "-555555555555555555 -1000000000000000000 1000000 1000000000000"
# 444445


def main():
    X, A, D, N = IL(case)

    # tgts = [(x * D + A) for x in range(N)]

    # 初項との差
    shokoDiff = A - X

    # 最終項との差
    lastDiff = (A + (D * (N - 1))) - X

    if (shokoDiff >= 0 and lastDiff >= 0) or (shokoDiff <= 0 and lastDiff <= 0):
        print(min([abs(shokoDiff), abs(lastDiff)]))
        return

    maybeMin = abs(shokoDiff) % D

    print(min([abs(maybeMin), abs(D - maybeMin)]))


if __name__ == "__main__":
    main()
