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
    (N,), *ABs = IALL(case)

    ratios: list[tuple[float, int]] = []

    for idx, x in enumerate(ABs, 1):
        tmp = (1 - (x[0] * 10**20 // (x[0] + x[1])), idx)
        ratios.append(tmp)

    ratios.sort()

    print(*[x[1] for x in ratios])


if __name__ == "__main__":
    main()
