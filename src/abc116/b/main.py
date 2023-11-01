#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


def f(i: int):
    if i % 2 == 0:
        return i // 2
    else:
        return i * 3 + 1


def main():
    S = int(case)

    existSet: set[int] = set()

    for x in range(1, 1000000000):
        if S in existSet:
            print(x)
            return

        else:
            existSet.add(S)
            S = f(S)

    pass


if __name__ == "__main__":
    main()
