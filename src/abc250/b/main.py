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
    N, A, B = IL(case)

    dotStart = [("." if idx % 2 == 1 else "#") * B for idx, x in enumerate(range(N), 1)]
    shpStart = [("." if idx % 2 == 0 else "#") * B for idx, x in enumerate(range(N), 1)]

    for idx, x in enumerate(range(N), 1):
        for y in range(A):
            print("".join(dotStart if idx % 2 == 1 else shpStart))


if __name__ == "__main__":
    main()
