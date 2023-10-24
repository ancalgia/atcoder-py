#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])
# case = "0"


def f(x: int) -> int:
    return (x**2) + (x * 2) + 3


def main():
    t = int(case)

    print(f(f(f(t) + t) + f(f(t))))


if __name__ == "__main__":
    main()
