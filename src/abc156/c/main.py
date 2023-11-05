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
    N, Xs = case.splitlines()

    N = int(N)

    Xs = list(map(int, Xs.split()))

    minX = min(Xs)
    maxX = max(Xs)

    curr_score = 0

    for pos in range(minX, maxX):
        pass
        tmp = sum([pow(x - pos, 2) for x in Xs])

        if tmp < curr_score or curr_score == 0:
            curr_score = tmp

    print(curr_score)


if __name__ == "__main__":
    main()
