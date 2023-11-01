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
    Ss = IL(case)

    if not all([right - left >= 0 for left, right in zip(Ss, Ss[1:])]):
        print("No")
        return

    if not (100 <= Ss[0] and Ss[-1] <= 675):
        print("No")
        return

    if not all([x % 25 == 0 for x in Ss]):
        print("No")
        return

    print("Yes")


if __name__ == "__main__":
    main()
