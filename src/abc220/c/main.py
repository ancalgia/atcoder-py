#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


# from textwrap import dedent

# case = dedent(
#     """
# 3
# 3 5 2
# 26
#     """
# ).strip()


def main():
    (N,), As, (X,) = IALL(case)

    sumA = sum(As)

    d, m = divmod(X, sumA)

    count = 0

    for a in As:
        count += 1

        m -= a

        if m < 0:
            break

    print((d * N) + count)


if __name__ == "__main__":
    main()
