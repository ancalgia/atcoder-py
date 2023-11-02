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
    (N, Q), *Queries = IALL(case)

    penaDict: dict[int, int] = dict()

    for x in range(1, N + 1):
        penaDict[x] = 0

    for q1, q2 in Queries:
        if q1 == 1:
            penaDict[q2] += 1
        elif q1 == 2:
            penaDict[q2] += 2
        else:
            print("Yes") if penaDict[q2] >= 2 else print("No")


if __name__ == "__main__":
    main()
