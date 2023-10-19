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
# 5 3
# 1 2 2 4 5
#     """
# ).strip()


def main():
    (N, K), Ps = IALL(case)

    big = 0

    sums: list[int] = [0]

    curr = 0

    for x in Ps:
        curr += x
        sums.append(curr)

    for x in range(N - K + 1):
        # tgtSumOld = sum(Ps[x : x + K])
        tgtSum = sums[x + K] - sums[x]

        big = max([big, tgtSum])

    result = (big + K) / 2

    print("{:.12f}".format(result))


if __name__ == "__main__":
    main()
