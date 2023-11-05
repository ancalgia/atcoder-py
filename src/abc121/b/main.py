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
    (N, M, C), Bs, *As = [list(map(int, x.split())) for x in case.splitlines()]

    count = 0

    for a in As:
        ans = sum([x * b for x, b in zip(a, Bs)]) + C

        count += 1 if ans > 0 else 0

    print(count)


if __name__ == "__main__":
    main()
