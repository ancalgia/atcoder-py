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
    (N, M), *LRs = IALL(case)

    pSum = [0 for x in range(N + 1)]

    for le, ri in LRs:
        pSum[le - 1] += 1
        pSum[ri] -= 1

    resultPsum: list[int] = []

    tmp = 0
    for x in pSum:
        tmp += x
        resultPsum.append(tmp)

    print(len([x for x in resultPsum if x == M]))
    pass


if __name__ == "__main__":
    main()
