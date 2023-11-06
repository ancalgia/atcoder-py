#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on

M = 998244353

case: str = "".join([x for x in sys.stdin])


def main():
    A, B, C, D, E, F = IL(case)

    result = ((((A % M) * (B % M) * (C % M)) % M) - ((D % M) * (E % M) * (F % M)) % M) % M

    print(result)


if __name__ == "__main__":
    main()
