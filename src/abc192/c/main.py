#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


def g1(i: int):
    s = str(i)

    return int("".join(sorted(s, reverse=True)))


def g2(i: int):
    s = str(i)

    return int("".join(sorted(s)))


def f(x: int):
    return g1(x) - g2(x)


def main():
    N, K = IL(case)

    curr = N

    for x in range(K):
        curr = f(curr)

    print(curr)


if __name__ == "__main__":
    main()
