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

    startWith0 = 0
    startWith1 = 0

    for idx, x in enumerate(S):
        if int(x) == idx % 2:
            startWith0 += 1

    for idx, x in enumerate(S):
        if int(x) == (idx + 1) % 2:
            startWith1 += 1

    print(min([startWith0, startWith1]))


if __name__ == "__main__":
    main()
