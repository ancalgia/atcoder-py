#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


sys.setrecursionlimit(10**9)

case: str = "".join([x for x in sys.stdin])

# from textwrap import dedent

# case = dedent(
#     """
# 7
# 6 7 2 1 3 4 5
#     """
# ).strip()


alreadyvisited: set[int] = set()


def walk(curr: int, fromtoDict: dict[int, int], trace: list[int], currentVisitSet: set[int]):
    if curr in currentVisitSet:
        tgtidx = trace.index(curr)

        print(len(trace[tgtidx:]))
        print(*trace[tgtidx:])
        exit()

    alreadyvisited.add(curr)
    currentVisitSet.add(curr)
    trace.append(curr)

    walk(fromtoDict[curr], fromtoDict, trace, currentVisitSet)


def main():
    (N,), As = IALL(case)

    fromtoDict: dict[int, int] = {}

    for idx, a in enumerate(As, 1):
        fromtoDict[idx] = a

    for idx in range(1, N + 1):
        if idx in alreadyvisited:
            continue

        trace: list[int] = []

        currentVisitSet: set[int] = set()

        walk(idx, fromtoDict, trace, currentVisitSet)

    # while len(alreadyvisited) != len(As):

    #     while True:

    pass


if __name__ == "__main__":
    main()
