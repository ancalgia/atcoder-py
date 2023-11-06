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
# 6
# abcbac
#     """
# ).strip()


def main():
    N, S = SL(case)

    N = int(N)

    for x in range(1, N):
        tmp = 0
        for y in range(0, N - x):
            if S[y] != S[y + x]:
                tmp += 1
            else:
                break

        print(tmp)


if __name__ == "__main__":
    main()
