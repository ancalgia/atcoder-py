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
    N, S = SL(case)

    N = int(N)

    X = 0

    maxX = 0

    for c in S:
        if c == "I":
            X += 1
            maxX = max([X, maxX])

        else:
            X -= 1

    print(maxX)


if __name__ == "__main__":
    main()
