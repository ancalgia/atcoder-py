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
# 10
# 3 3 3 3 4 4 4 5 5 5
#     """
# ).strip()


def main():
    (N,), As = IALL(case)

    AsCounter = collections.Counter(As)

    over2s = [x for x in AsCounter if AsCounter[x] >= 2]
    over4s = [x for x in AsCounter if AsCounter[x] >= 4]

    over2s.sort(reverse=True)
    over4s.sort(reverse=True)

    choho = 0
    if len(over2s) >= 2:
        choho = over2s[0] * over2s[1]

    seho = 0
    if len(over4s) >= 1:
        seho = over4s[0] ** 2

    print(max(choho, seho))


if __name__ == "__main__":
    main()
