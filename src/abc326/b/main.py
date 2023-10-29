#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


def isLikeNumber(i: int):
    strI = str(i)

    if int(strI[0]) * int(strI[1]) == int(strI[2]):
        return True

    return False


def main():
    N = int(case)

    while True:
        if isLikeNumber(N):
            print(N)
            return

        N += 1


if __name__ == "__main__":
    main()
