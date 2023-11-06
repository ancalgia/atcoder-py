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
    N = int(case)

    results: list[list[int]] = [[1]]

    for x in range(N - 1):
        tmp = [0] + results[-1].copy() + [0]

        sums = [right + left for left, right in zip(tmp, tmp[1:])]

        results.append(sums)

    for x in results:
        print(*x)


if __name__ == "__main__":
    main()
