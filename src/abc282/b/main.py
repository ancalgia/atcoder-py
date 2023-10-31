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
    NM, *OXs = SL(case)

    allPtn = itertools.combinations(OXs, 2)

    result = 0

    for x in allPtn:
        zipped = zip(*x)

        if all([True if y[0] == "o" or y[1] == "o" else False for y in zipped]):
            result += 1

    print(result)


if __name__ == "__main__":
    main()
