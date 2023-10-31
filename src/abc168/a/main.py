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
    N, *_ = SL(case)

    tgt = int(N[-1])

    if tgt in [2, 4, 5, 7, 9]:
        print("hon")
    elif tgt in [0, 1, 6, 8]:
        print("pon")
    else:
        print("bon")


if __name__ == "__main__":
    main()
