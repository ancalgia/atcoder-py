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
    N, M = IL(case)

    ptns = {x for x in range(1, M + 1)}

    allPtn = list(itertools.combinations(ptns, N))

    result = []

    for x in allPtn:
        if all([right - left for left, right in zip(x, x[1:])]):
            result.append(x)

    result.sort()

    for x in result:
        print(*x)

    pass


if __name__ == "__main__":
    main()
