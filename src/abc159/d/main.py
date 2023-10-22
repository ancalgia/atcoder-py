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
    N, As = IALL(case)

    AsSet = set(As)

    AsCounter = collections.Counter(As)

    resultDict: dict[int, int] = dict()

    normalResult = sum([math.comb(AsCounter[y], 2) for y in AsCounter if y != 0])

    for x in AsSet:
        if AsCounter[x] == 1:
            resultDict[x] = normalResult

        else:
            # resultDict[x] = sum([math.comb(AsCounter[y] - (1 if x == y else 0), 2) for y in AsCounter if y != 0])
            resultDict[x] = normalResult - (AsCounter[x] - 1)
    for x in As:
        print(resultDict[x])


if __name__ == "__main__":
    main()
