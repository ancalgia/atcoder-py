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
    (N,), Xs = IALL(case)

    sortedXs = sorted(Xs)

    centerLeft = sortedXs[(N // 2) - 1]
    centerRight = sortedXs[(N // 2)]

    if centerLeft == centerRight:
        [print(centerRight) for x in range(N)]
        return

    for p in Xs:
        if p <= centerLeft:
            print(centerRight)
        else:
            print(centerLeft)

    pass


if __name__ == "__main__":
    main()
