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
    A, B, C, D, E, F, X = IL(case)

    d1, m1 = divmod(X, (A + C))
    takaDist = (d1 * (A * B)) + min([(m1 * B), (A * B)])

    d2, m2 = divmod(X, (D + F))
    aokiDist = (d2 * (D * E)) + min([(m2 * E), (D * E)])

    if takaDist == aokiDist:
        print("Draw")
        return

    print("Takahashi") if takaDist > aokiDist else print("Aoki")


if __name__ == "__main__":
    main()
