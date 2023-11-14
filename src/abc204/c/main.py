#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


gABs: set[tuple[int, int]]


# def getAllAbles(start: int, routes: set[tuple[int, int]]) -> int:
def getAllAbles(start: int) -> int:
    resultSet: set[int] = set([start])

    nextAbles: set[int] = set([start])

    global gABs

    while True:
        currentAbles: set[int] = set()

        for x in nextAbles:
            for a, b in gABs:
                if a == x:
                    if b not in resultSet:
                        currentAbles.add(b)
                        resultSet.add(b)

        if len(currentAbles) == 0:
            [gABs.add((start, x)) for x in resultSet]

            return len(resultSet)

        nextAbles = currentAbles


def main():
    (N, M), *ABs = IALL(case)

    result = 0

    global gABs

    gABs = set([(a, b) for a, b in ABs])

    for start in range(1, N + 1):
        result += getAllAbles(start)

    print(result)


if __name__ == "__main__":
    main()
