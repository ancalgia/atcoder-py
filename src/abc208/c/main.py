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
    (N, K), As = IALL(case)

    AsWithIdx = [x for x in enumerate(As)]

    AsWithIdx.sort(key=lambda x: x[1])

    allPpl, modd = divmod(K, N)

    omakeList = set()

    for x in range(modd):
        omakeList.add(AsWithIdx[x][1])

    for x in As:
        print(allPpl + (1 if x in omakeList else 0))


if __name__ == "__main__":
    main()
