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
    (M, D), (y, m, d) = IALL(case)

    if d == D:
        d = 1
        m += 1
    else:
        d += 1

    if m == M + 1:
        m = 1
        y += 1

    print(*[y, m, d])


if __name__ == "__main__":
    main()
