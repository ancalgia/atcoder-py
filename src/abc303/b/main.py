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
    (N, M), *As = IALL(case)

    friendSet: set[tuple[int, int]] = set()

    allPtnCount = (N * (N - 1)) // 2

    for a in As:
        for x in range(N - 1):
            le = min([a[x], a[x + 1]])
            ri = max([a[x], a[x + 1]])

            friendSet.add((le, ri))

    print(allPtnCount - len(friendSet))


if __name__ == "__main__":
    main()
