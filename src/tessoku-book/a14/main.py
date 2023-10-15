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
    (N, K), As, Bs, Cs, Ds = IALL(case)

    ABs = set(itertools.product(As, Bs))

    CDs = set(itertools.product(Cs, Ds))

    sumABs = set([sum(x) for x in ABs])

    sumCDs = set([sum(x) for x in CDs])

    # ABCDs = set(itertools.product(sumABs, sumCDs))

    for x in sumABs:
        if (K - x) in sumCDs:
            print("Yes")
            return

    print("No")

    # sumABCDs = set([sum(x) for x in ABCDs])

    # if K in sumABCDs:
    #     print("Yes")
    # else:
    #     print("No")

    pass


if __name__ == "__main__":
    main()
