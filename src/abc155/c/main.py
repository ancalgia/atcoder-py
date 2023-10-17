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
    N, *Ss = SL(case)

    counter = collections.Counter(Ss)

    descended = list(counter.most_common())

    most = descended[0][1]

    populars: list[str] = []

    for x in descended:
        if x[1] == most:
            populars.append(x[0])

    sortedPopulars = sorted(populars)

    [print(x) for x in sortedPopulars]


if __name__ == "__main__":
    main()
