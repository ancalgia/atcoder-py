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
    (N, L, R), As = IALL(case)

    results = []

    for a in As:
        if a < L:
            results.append(L)

        elif a > R:
            results.append(R)

        else:
            results.append(a)

    print(*results)


if __name__ == "__main__":
    main()
