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
    N = int(case)

    # 1 回目から  125 回目までは  4 問
    # 126 回目から  211 回目までは  6 問
    # 212 回目から  214 回目までは  8 問

    if N <= 125:
        print(4)
    elif N <= 211:
        print(6)
    else:
        print(8)


if __name__ == "__main__":
    main()
