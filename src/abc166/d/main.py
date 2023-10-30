#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])

# case = "1000000000"
# case = "9898756454"


def main():
    X = int(case)

    patterns: set[tuple[int, int]] = set()

    for x in range(X + 100):
        tmp = x**5

        if tmp < (X + 1) * 100:
            patterns.add((tmp, x))
            patterns.add((-tmp, -x))
            continue
        else:
            break

    allComb = itertools.combinations(patterns, 2)

    for a, b in allComb:
        if a[0] - b[0] == X:
            print(f"{a[1]} {b[1]}")
            return
        if b[0] - a[0] == X:
            print(f"{b[1]} {a[1]}")
            return


if __name__ == "__main__":
    main()
