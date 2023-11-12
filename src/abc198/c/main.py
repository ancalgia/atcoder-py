#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


# case = "100 0 1"


def main():
    R, X, Y = IL(case)

    allDist = math.sqrt(X**2 + Y**2)

    d, m = divmod(allDist, R)

    if d == 0:
        print(2)
        return

    if m == 0:
        print(int(d))

    else:
        print(int(d) + 1)

    # print(math.ceil(allDist / R))

    pass


if __name__ == "__main__":
    main()
