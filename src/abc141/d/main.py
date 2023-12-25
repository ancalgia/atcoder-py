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
    (N, M), As = IALL(case)

    hpAs: list[int] = []

    heapq.heapify(hpAs)

    for a in As:
        heapq.heappush(hpAs, -a)

    for _x in range(M):
        maxPrice = heapq.heappop(hpAs)
        heapq.heappush(hpAs, maxPrice / 2)

    print(sum(map(int, map(abs, hpAs))))


if __name__ == "__main__":
    main()
