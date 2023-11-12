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
    N, *Ss = SL(case)

    Ss = list(map(int, Ss))

    Ss.sort()

    allScore = sum(Ss)
    if allScore % 10 != 0:
        print(allScore)
        return

    for x in Ss:
        if x % 10 != 0:
            print(allScore - x)
            return

    print(0)


if __name__ == "__main__":
    main()
