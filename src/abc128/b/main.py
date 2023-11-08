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
    N, *SPs = SL(case)

    N = int(N)

    SPs = [[x.split()[0], int(x.split()[1]), idx] for idx, x in enumerate(SPs, 1)]

    SPs.sort(key=lambda x: (x[0], -x[1]))

    [print(x[2]) for x in SPs]


if __name__ == "__main__":
    main()
