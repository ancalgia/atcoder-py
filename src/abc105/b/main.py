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

    ables = {4, 7, 8, 11, 12, 14, 15, 16, 18, 19, 20, 21}

    print("Yes") if N in ables or N >= 20 else print("No")


if __name__ == "__main__":
    main()
