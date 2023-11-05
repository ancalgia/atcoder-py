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
    NW, As = case.splitlines()

    N, W = list(map(int, NW.split()))

    As = list(map(int, As.split()))

    good_numbers: list[int] = []

    select1 = list(itertools.combinations(As, 1))

    good_numbers.extend([sum(x) for x in select1 if sum(x) <= W])

    if N < 2:
        print(len(set(good_numbers)))
        return

    select2 = list(itertools.combinations(As, 2))

    good_numbers.extend([sum(x) for x in select2 if sum(x) <= W])

    if N < 3:
        print(len(set(good_numbers)))
        return

    select3 = list(itertools.combinations(As, 3))

    good_numbers.extend([sum(x) for x in select3 if sum(x) <= W])

    print(len(set(good_numbers)))


if __name__ == "__main__":
    main()
