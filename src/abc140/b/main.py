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
    (N,), As, Bs, Cs = [list(map(int, x.split())) for x in case.splitlines()]

    manzoku = 0

    last_food = 99999

    for x in As:
        manzoku += Bs[x - 1]

        if last_food + 1 == x:
            manzoku += Cs[last_food - 1]

        last_food = x

    print(manzoku)

    pass


if __name__ == "__main__":
    main()
