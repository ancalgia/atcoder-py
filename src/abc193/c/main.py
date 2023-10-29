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

    excepts: set[int] = set({})

    # for x in range(2, N):
    for x in range(2, math.ceil(math.sqrt(N)) + 2):
        for y in range(2, N):
            tgt = x**y
            if tgt <= N:
                excepts.add(tgt)

            else:
                break

    print(N - len(excepts))


if __name__ == "__main__":
    main()
