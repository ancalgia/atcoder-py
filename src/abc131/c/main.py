#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


# case = "10 40 6 8 "


def main():
    A, B, C, D = IL(case)

    divC = (B // C) - ((A - 1) // C)
    divD = (B // D) - ((A - 1) // D)
    divCD = (B // (math.lcm(C, D))) - ((A - 1) // math.lcm(C, D))

    allCount = B - A + 1

    print(allCount - divC - divD + divCD)


if __name__ == "__main__":
    main()
