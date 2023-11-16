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
    (N, M), *ABs = IALL(case)

    from1 = set()

    toN = set()

    for a, b in ABs:
        if a == 1:
            from1.add(b)
        elif b == 1:
            from1.add(a)
        elif a == N:
            toN.add(b)
        elif b == N:
            toN.add(a)

    cond = len(from1 & toN) >= 1

    print("POSSIBLE") if cond else print("IMPOSSIBLE")


if __name__ == "__main__":
    main()
