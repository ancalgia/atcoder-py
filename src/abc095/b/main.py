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
    NX, *rest = case.splitlines()

    N, X = map(int, NX.split())

    donuts = list(map(int, rest))

    make_count = N

    left_zairyo = X - sum(donuts)

    min_donut = min(donuts)

    make_count += left_zairyo // min_donut

    print(make_count)


if __name__ == "__main__":
    main()
