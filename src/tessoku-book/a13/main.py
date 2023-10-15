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
# 7 10
# 11 12 16 22 27 28 31
# """
# ).strip()


def main():
    (N, K), As = IALL(case)

    count = 0

    br = bisect.bisect_right

    for x in range(N - 1):
        tmp = br(As[x:], As[x] + K)

        count += tmp - 1

    print(count)


if __name__ == "__main__":
    main()
