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
    L1, R1, L2, R2 = IL(case)

    red = set([x for x in range(L1, R1)])
    blue = set([x for x in range(L2, R2)])

    print(len(red & blue))


if __name__ == "__main__":
    main()
