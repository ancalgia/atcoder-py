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
# 5
# 1 3 5 4 2
#     """
# ).strip()


def main():
    (N,), Ps = IALL(case)

    result = 0

    for x in range(N - 2):
        if sorted(Ps[x : x + 3])[1] == Ps[x + 1]:
            result += 1

    print(result)


if __name__ == "__main__":
    main()
