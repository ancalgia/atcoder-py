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
    A, B = IL(case)

    setA = {1, 3, 5, 7, 8, 10, 12}
    setB = {4, 6, 9, 11}

    print("Yes") if (A in setA and B in setA) or (A in setB and B in setB) else print("No")


if __name__ == "__main__":
    main()
