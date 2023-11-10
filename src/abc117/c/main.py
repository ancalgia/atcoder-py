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
# 4 3
# -100000 5 99999
#     """
# ).strip()


def main():
    (N, M), Xs = IALL(case)

    if N >= M:
        print(0)
        return

    Xs.sort()

    distances = [right - left for left, right in zip(Xs, Xs[1:])]

    distances.sort()

    print(sum(distances[: M - N]))


if __name__ == "__main__":
    main()
