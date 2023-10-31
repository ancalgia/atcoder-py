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

    le = 1
    ri = N

    while True:
        if le == ri:
            print(le)
            return

        tgt = (le + ri) // 2

        today = ((1 + tgt) * tgt) // 2

        if today < N:
            if ri - le == 1:
                le += 1
            else:
                le = tgt
        else:
            if ri - le == 1:
                ri -= 1
            else:
                ri = tgt


if __name__ == "__main__":
    main()
