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
    X, Y, A, B = IL(case)

    exp = 0

    # isMinus1 = True

    if X * A >= Y and X + B >= Y:
        print(0)
        return

    while X < Y:
        if X * A < X + B:
            X *= A
            exp += 1

        else:
            exp += (Y - X - 1) // B
            break

    print(exp)


if __name__ == "__main__":
    main()
