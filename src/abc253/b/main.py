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
    HW, *rest = SL(case)

    H, W = map(int, HW.split())

    martix = [list(x) for x in rest]

    point = []

    for x in range(H):
        for y in range(W):
            if martix[x][y] == "o":
                point.append([x, y])

    print(abs(point[0][0] - point[1][0]) + abs(point[0][1] - point[1][1]))

    pass


if __name__ == "__main__":
    main()
