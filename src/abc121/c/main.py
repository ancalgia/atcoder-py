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
    (N, M), *ABs = IALL(case)

    ABs.sort()

    money = 0

    needs = M

    for a, b in ABs:
        if needs <= b:
            money += needs * a
            break

        else:
            money += a * b
            needs -= b

    print(money)


if __name__ == "__main__":
    main()
