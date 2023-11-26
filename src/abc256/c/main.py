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
    H1, H2, H3, W1, W2, W3 = IL(case)

    maybeH1: list[tuple[int, int, int]] = []
    maybeH2: list[tuple[int, int, int]] = []
    maybeH3: list[tuple[int, int, int]] = []

    for x in range(1, H1):
        for y in range(1, H1):
            if x + y > H1:
                break
            z = H1 - x - y
            if z >= 1:
                maybeH1.append((x, y, z))

    for x in range(1, H2):
        for y in range(1, H2):
            if x + y > H2:
                break
            z = H2 - x - y
            if z >= 1:
                maybeH2.append((x, y, z))

    for x in range(1, H3):
        for y in range(1, H3):
            if x + y > H3:
                break
            z = H3 - x - y
            if z >= 1:
                maybeH3.append((x, y, z))

    allPtn = itertools.product(maybeH1, maybeH2, maybeH3)

    result = 0

    for p, t, n in allPtn:
        if p[2] + t[2] + n[2] != W3:
            continue
        if p[0] + t[0] + n[0] != W1:
            continue
        if p[1] + t[1] + n[1] != W2:
            continue
        result += 1

    print(result)


if __name__ == "__main__":
    main()
