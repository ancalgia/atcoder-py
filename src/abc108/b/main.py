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
    X1, Y1, X2, Y2 = IL(case)

    # X3 = X1 + (X2 - X1) + (Y2 - Y1)
    X3 = X1 + ((X2 - X1) - (Y2 - Y1))
    Y3 = Y1 + ((Y2 - Y1) + (X2 - X1))
    X4 = X2 + ((X3 - X2) - (Y3 - Y2))
    Y4 = Y2 + ((Y3 - Y2) + (X3 - X2))

    print(f"{X3} {Y3} {X4} {Y4}")


if __name__ == "__main__":
    main()
