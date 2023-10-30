#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


waters = 0


def divide(lis: list[int]) -> list[list[int]]:
    result: list[list[int]] = []
    chunk: list[int] = []

    for x in lis:
        if x == 0:
            if len(chunk) != 0:
                result.append(chunk.copy())
                chunk.clear()
            continue

        else:
            chunk.append(x)

    if len(chunk) != 0:
        result.append(chunk.copy())

    return result


def shower(lis: list[int]):
    minWater = min(lis)

    lis = [x - minWater for x in lis]

    global waters
    waters += minWater

    return lis


def main():
    (N,), Hs = IALL(case)

    Hs = [Hs]

    while True:
        Hs = list(itertools.chain.from_iterable([divide(x) for x in Hs]))

        if len(Hs) == 0:
            print(waters)
            return

        Hs = [shower(x) for x in Hs]


if __name__ == "__main__":
    main()
