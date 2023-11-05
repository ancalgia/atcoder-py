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
    (X1, Y1), (X2, Y2), (X3, Y3) = IALL(case)

    XCounter = collections.Counter([X1, X2, X3]).most_common()
    YCounter = collections.Counter([Y1, Y2, Y3]).most_common()

    print(f"{XCounter[1][0]} {YCounter[1][0]}")


if __name__ == "__main__":
    main()
