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
    NX, S = SL(case)

    N, X = IL(NX)

    current = X

    for x in S:
        if x == "o":
            current += 1
        else:
            current -= 1
            current = max([0, current])

    print(current)


if __name__ == "__main__":
    main()
