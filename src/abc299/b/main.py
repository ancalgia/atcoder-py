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
    (N, T), Cs, Rs = IALL(case)

    CRs = set([x for x in enumerate(zip(Cs, Rs), 1)])

    tgt = T if T in Cs else Cs[0]

    currMax = 0

    currWin = 0

    for x in CRs:
        if x[1][0] == tgt:
            if currMax < x[1][1]:
                currMax = x[1][1]
                currWin = x[0]

    print(currWin)


if __name__ == "__main__":
    main()
