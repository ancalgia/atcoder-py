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
    N, As, Bs = SL(case)

    As = As.split()
    Bs = Bs.split()

    Counts = collections.Counter(As + Bs)

    combSet = set()

    samePosCombSet = set()

    for x in Counts:
        if Counts[x] == 2:
            combSet.add(x)

    for a, b in zip(As, Bs):
        if a == b:
            combSet.remove(a)
            samePosCombSet.add(a)

    print(len(samePosCombSet))
    print(len(combSet))


if __name__ == "__main__":
    main()
