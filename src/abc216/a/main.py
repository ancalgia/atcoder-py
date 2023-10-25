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
    XY = case.rstrip()

    X, Y = XY[:-2], int(XY[-1:])

    if Y <= 2:
        print(X + "-")
    elif Y <= 6:
        print(X)
    else:
        print(X + "+")


if __name__ == "__main__":
    main()
