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
    N, As, Bs, Cs = IALL(case)

    BCDict: dict[int, int] = dict()

    for idx, c in enumerate(Cs):
        BCDict[idx] = Bs[c - 1]

    BCounter = collections.Counter(BCDict.values())

    result = 0

    for a in As:
        result += BCounter[a]

    print(result)


if __name__ == "__main__":
    main()
