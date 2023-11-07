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
    N, S = SL(case)
    N = int(N)

    result = 0

    for pos in range(N):
        x = S[:pos]
        y = S[pos:]

        xSet = set(x)
        ySet = set(y)

        tmp = len(xSet & ySet)

        result = max([result, tmp])

    print(result)


if __name__ == "__main__":
    main()
