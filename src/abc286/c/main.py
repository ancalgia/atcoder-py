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
# 5 1 2
# rrefa
#     """
# ).strip()


def main():
    NAB, S = SL(case)

    N, A, B = IL(NAB)

    S = S + S

    result = 10**20

    for x in range(N):
        rotatePrice = x * A

        tgt = S[x : x + N]
        # print(tgt)

        diffCount = math.ceil(len([1 for x, y in zip(tgt, tgt[::-1]) if x != y]) / 2)
        altPrice = diffCount * B

        result = min(result, rotatePrice + altPrice)

    print(result)


if __name__ == "__main__":
    main()
