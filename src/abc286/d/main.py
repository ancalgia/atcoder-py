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
    (N, X), *ABs = IALL(case)

    dpSet = {0}

    coins = list(itertools.chain.from_iterable([[a for _ in range(b)] for a, b in ABs]))

    for x in coins:
        for s in list(dpSet):
            dpSet.add(s + x)

        if X in dpSet:
            print("Yes")
            return

    print("No")


if __name__ == "__main__":
    main()
