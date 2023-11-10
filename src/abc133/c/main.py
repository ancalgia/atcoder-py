#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])

# case = "674 680"


def main():
    L, R = IL(case)

    if L == 0:
        print(0)
        return

    existSet = set()

    for x in range(4100):
        if L + x > R:
            break

        tmp = (L + x) % 2019

        if tmp not in existSet:
            existSet.add(tmp)
        else:
            break

    testComb = itertools.combinations(existSet, 2)

    print(min([(x * y) % 2019 for x, y in testComb]))


if __name__ == "__main__":
    main()
