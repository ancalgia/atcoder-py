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

    elapsed_years = 0

    depo = 100

    if depo >= N:
        print(0)
        return

    while 1:
        elapsed_years += 1
        # depo = math.floor(depo * 1.01)
        depo += depo // 100

        if depo >= N:
            break

    print(elapsed_years)


if __name__ == "__main__":
    main()
