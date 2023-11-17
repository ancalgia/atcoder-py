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
    A, B, C, X, Y = IL(case)

    isAMoreNeeded = X > Y

    samePizzaCount = min(X, Y)

    morePizzaCount = abs(X - Y)

    samePizzaPrice = min(samePizzaCount * (A + B), samePizzaCount * (C * 2))

    morePizzaPrice = min(morePizzaCount * (A if isAMoreNeeded else B), morePizzaCount * (C * 2))

    print(samePizzaPrice + morePizzaPrice)


if __name__ == "__main__":
    main()
