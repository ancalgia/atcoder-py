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
    X, Y = IL(case)

    maxAsi = X * 4
    minAsi = X * 2

    if Y % 2 == 1:
        print("No")
        return

    if Y > maxAsi:
        print("No")
        return

    if Y < minAsi:
        print("No")
        return

    print("Yes")


if __name__ == "__main__":
    main()
