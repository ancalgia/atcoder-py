#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])
# case = 191


def main():
    N = int(case)

    price = math.floor(N * 1.08)

    if price < 206:
        print("Yay!")
    elif price == 206:
        print("so-so")
    else:
        print(":(")


if __name__ == "__main__":
    main()
