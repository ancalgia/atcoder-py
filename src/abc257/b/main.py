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
    (N, K, Q), As, Ls = [list(map(int, x.split())) for x in case.splitlines()]

    for x in Ls:
        if As[x - 1] == N:
            continue
        if As[x - 1] + 1 in As:
            continue

        As[x - 1] += 1

    print(" ".join(map(str, As)))


if __name__ == "__main__":
    main()
