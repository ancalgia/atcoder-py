#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


# case = "2 5 4"


def main():
    A, B, C = IL(case)

    ABC = sorted([A, B, C])

    Diff1 = ABC[2] - ABC[0]
    Diff2 = ABC[2] - ABC[1]

    d, m = divmod(Diff1 + Diff2, 2)

    print(d + (m * 2))


if __name__ == "__main__":
    main()
