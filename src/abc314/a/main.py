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

    pi1 = "3."
    pi2 = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

    print(pi1 + pi2[:N])

    pass


if __name__ == "__main__":
    main()
