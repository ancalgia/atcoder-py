#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


def format_a(a: list[int]) -> list[int]:
    if a[0] == 1:
        return [a[1] * 2, a[2] * 2]
    if a[0] == 2:
        return [a[1] * 2, a[2] * 2 - 1]
    if a[0] == 3:
        return [a[1] * 2 + 1, a[2] * 2]
    if a[0] == 4:
        return [a[1] * 2 + 1, a[2] * 2 - 1]

    raise Exception


case: str = "".join([x for x in sys.stdin])


def main():
    (N,), *As = [list(map(int, x.split())) for x in case.splitlines()]

    formattedAs = [format_a(x) for x in As]

    count = 0

    for x_idx in range(N):
        for y_idx in range(x_idx + 1, N):
            if formattedAs[x_idx][0] <= formattedAs[y_idx][1] and formattedAs[x_idx][1] >= formattedAs[y_idx][0]:
                count += 1

    print(count)


if __name__ == "__main__":
    main()
