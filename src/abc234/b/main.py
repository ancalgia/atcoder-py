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

    result = 0

    for x1, y1 in XYs:
        for x2, y2 in XYs:
            dist = math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)

            result = max([result, dist])

    print(result)

    pass


if __name__ == "__main__":
    main()
