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
# 3 4
# 2 1 3
# 3 1 2 3
# 2 3 2
#     """
# ).strip()


def main():
    (N, M), *ANs = IALL(case)

    ANs = [rest for x, *rest in ANs]

    ANSets: list[set[int]] = []

    for an in ANs:
        ANSets.append(set(an))

    everyLikes = set([x for x in range(1, M + 1)])

    for s in ANSets:
        everyLikes = everyLikes & s

    print(len(everyLikes))


if __name__ == "__main__":
    main()
