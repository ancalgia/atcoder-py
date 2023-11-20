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
    (N, M), *PYs = IALL(case)

    pass

    YPIdx = [(y, p, idx) for idx, (p, y) in enumerate(PYs, 1)]

    YPIdx.sort()

    results: dict[int, str] = {}

    counter: collections.Counter[int] = collections.Counter()

    for y, p, idx in YPIdx:
        counter[p] += 1

        results[idx] = f"{str(p).zfill(6)}{str(counter[p]).zfill(6)}"

    for x in range(1, M + 1):
        if x in results:
            print(results[x])


if __name__ == "__main__":
    main()
