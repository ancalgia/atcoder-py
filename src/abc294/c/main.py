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
    (N, M), As, Bs = IALL(case)

    Cs = sorted(As + Bs)

    cDict: dict[int, int] = dict()

    for idx, x in enumerate(Cs, 1):
        cDict[x] = idx

    print(*[cDict[x] for x in As])
    print(*[cDict[x] for x in Bs])


if __name__ == "__main__":
    main()
