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
# 1 2
#     """
# ).strip()


def main():
    (N,), Ps = IALL(case)

    Ps = [0] + Ps

    current = N - 1

    result = 0

    while True:
        next = Ps[current] - 1
        result += 1

        if next == 0:
            print(result)
            return

        current = next


if __name__ == "__main__":
    main()
