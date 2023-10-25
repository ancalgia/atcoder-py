#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on
MOD = 1000000007

case: str = "".join([x for x in sys.stdin])


def main():
    (N,), Cs = IALL(case)

    Cs.sort()

    result = 1

    for idx, x in enumerate(Cs):
        tmp = x - idx

        if tmp <= 0:
            print(0)
            return

        result *= tmp

        result %= MOD

    print(result)

    pass


if __name__ == "__main__":
    main()
