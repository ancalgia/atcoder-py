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

    min = 0.0
    max = 100000.0

    while True:
        if abs(min - max) < 0.00001:
            print(round(min, 6))
            return

        tgt = (min + max) / 2

        if ((tgt**3) + tgt) > N:
            max = tgt
        elif ((tgt**3) + tgt) < N:
            min = tgt


if __name__ == "__main__":
    main()
