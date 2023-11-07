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
    (N,), (K,), Xs = IALL(case)

    result = 0

    for x in Xs:
        tmp = min([(K - x) * 2, x * 2])

        result += tmp

    print(result)


if __name__ == "__main__":
    main()
