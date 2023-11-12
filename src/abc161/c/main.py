#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


# case = "2 6"
# 2


def main():
    N, K = IL(case)

    if N == 0:
        print(0)
        return

    if K == 1:
        print(0)
        return

    naturalSmall1 = N % K

    print(min([naturalSmall1, abs(naturalSmall1 - K)]))
    return


if __name__ == "__main__":
    main()
