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
    (N, M), As = IALL(case)

    so = sum(As)

    selectables = [x for x in As if x >= (so / (4 * M))]

    if len(selectables) >= M:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
