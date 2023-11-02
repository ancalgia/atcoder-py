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
# 3 3
# oxo
# oxo
# oxo
#     """
# ).strip()


def main():
    ND, *Ss = SL(case)

    maxChain = 0

    tmpChain = 0

    for x in zip(*Ss):
        if all([z == "o" for z in x]):
            tmpChain += 1
            maxChain = max([maxChain, tmpChain])

        else:
            tmpChain = 0

    print(maxChain)


if __name__ == "__main__":
    main()
