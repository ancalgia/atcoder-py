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
    (N,), As = IALL(case)

    # レート1-399：灰色
    # レート400-799：茶色
    # レート800-1199：緑色
    # レート1200-1599：水色
    # レート1600-1999：青色
    # レート2000-2399：黄色
    # レート2400-2799：橙色
    # レート2800-3199：赤色

    separated = set()

    anyColor = 0

    for a in As:
        if a < 400:
            separated.add(1)
        elif a < 800:
            separated.add(2)
        elif a < 1200:
            separated.add(3)
        elif a < 1600:
            separated.add(4)
        elif a < 2000:
            separated.add(5)
        elif a < 2400:
            separated.add(6)
        elif a < 2800:
            separated.add(7)
        elif a < 3200:
            separated.add(8)

        else:
            anyColor += 1

    if len(separated) == 0:
        print(f"1 {anyColor}")
    else:
        print(f"{len(separated)} {len(separated)+anyColor}")


if __name__ == "__main__":
    main()
