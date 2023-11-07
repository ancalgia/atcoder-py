#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


# "8 13"


def main():
    A, B = IL(case)

    diff = B - A

    fullTall = ((1 + diff) * diff) // 2

    print(fullTall - B)


if __name__ == "__main__":
    main()
