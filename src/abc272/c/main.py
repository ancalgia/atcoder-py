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
    N, As = IALL(case)

    OddList = sorted([x for x in As if x % 2 == 1])

    EvenList = sorted([x for x in As if x % 2 == 0])

    result = -1

    if len(OddList) >= 2:
        result = max([result, OddList[-1] + OddList[-2]])

    if len(EvenList) >= 2:
        result = max([result, EvenList[-1] + EvenList[-2]])

    print(result)


if __name__ == "__main__":
    main()
