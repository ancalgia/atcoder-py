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
    (N,), Ps = [list(map(int, x.split())) for x in case.splitlines()]

    ng_count = 0

    for idx, x in enumerate(Ps, 1):
        if idx != x:
            ng_count += 1

    print("YES" if ng_count == 0 or ng_count == 2 else "NO")


if __name__ == "__main__":
    main()
