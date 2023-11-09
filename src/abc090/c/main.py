#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


def main():
    N, M = IL(case)

    if N == 1 and M == 1:
        print(1)
        return

    if N == 1 or M == 1:
        print(N * M - 2)
        return

    if N == 2 or M == 2:
        print(0)
        return

    print((N - 2) * (M - 2))


if __name__ == "__main__":
    main()
