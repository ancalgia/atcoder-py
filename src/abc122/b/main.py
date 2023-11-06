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
    S, *_ = SL(case)

    tmp = 0
    maxChain = 0

    for c in S:
        if c in ["A", "C", "G", "T"]:
            tmp += 1
            maxChain = max([maxChain, tmp])
        else:
            tmp = 0

    print(maxChain)


if __name__ == "__main__":
    main()
