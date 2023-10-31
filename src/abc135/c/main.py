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
    N, As, Bs = IALL(case)

    Bs = Bs + [0]

    tmp = 0
    result = 0

    for a, b in zip(As, Bs):
        tmp += a

        if tmp < 0:
            result += tmp
            tmp = 0

        result += b
        tmp -= b

        if tmp > 0:
            tmp = 0

    print(result)


if __name__ == "__main__":
    main()
