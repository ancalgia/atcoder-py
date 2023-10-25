#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


# case = "119"


def main():
    N = int(case)

    kokaList = [math.factorial(x + 1) for x in range(10)][::-1]

    result = 0

    rest = N

    while True:
        if rest == 0:
            print(result)
            return

        for x in kokaList:
            if rest >= x:
                rest -= x
                result += 1
                break


if __name__ == "__main__":
    main()
