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
    (N, K), *ABs = IALL(case)

    left = 1

    right = max([x[1] for x in ABs])

    result = 9999999

    while True:
        tgt = (right + left) // 2

    pass


if __name__ == "__main__":
    main()
