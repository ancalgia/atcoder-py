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
    X, Y, N = IL(case)

    if X * 3 <= Y:
        print(X * N)
        return

    d, m = divmod(N, 3)

    Ys = Y * d

    Xs = X * m

    print(Ys + Xs)


if __name__ == "__main__":
    main()
