#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


# case = "1 1000000000 100"


def main():
    A, B, K = IL(case)

    # seq = [x for x in range(A, B + 1)]

    leAndRi = list(set([x for x in range(A, A + K)] + [x for x in range(B, B - K, -1)]))

    leAndRi.sort()

    [print(x) for x in leAndRi if A <= x <= B]


if __name__ == "__main__":
    main()
