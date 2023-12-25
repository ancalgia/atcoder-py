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
    (N,), *XYs = IALL(case)

    # print(XYs)

    resultSet: set[tuple[int, int]] = set()

    for a in range(N):
        for b in range(a + 1, N):
            cityA = XYs[a]
            cityB = XYs[b]

            xDist = cityB[0] - cityA[0]
            yDist = cityB[1] - cityA[1]

            gcd = math.gcd(abs(xDist), abs(yDist))

            xDist //= gcd
            yDist //= gcd

            resultSet.add((xDist, yDist))
            resultSet.add((-xDist, -yDist))

    print(len(resultSet))


if __name__ == "__main__":
    main()
