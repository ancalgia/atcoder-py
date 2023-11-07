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
    (N,), Ts, (M,), *PXs = IALL(case)

    for p, x in PXs:
        tmp = 0
        for idx, t in enumerate(Ts, 1):
            if idx == p:
                tmp += x
            else:
                tmp += t

        print(tmp)


if __name__ == "__main__":
    main()
