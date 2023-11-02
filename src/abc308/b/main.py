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
    NM, Cs, Ds, Ps = SL(case)

    N, M = IL(NM)

    Cs = Cs.split()
    Ds = Ds.split()
    elseP, *Ps = IL(Ps)

    priceDict: dict[str, int] = dict()
    for d, p in zip(Ds, Ps):
        priceDict[d] = p

    result = 0
    for c in Cs:
        result += priceDict.get(c, elseP)

    print(result)


if __name__ == "__main__":
    main()
