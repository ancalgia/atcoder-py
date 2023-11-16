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
# 1 2 3 4
# 1 3
# 2 3
# 2 4
#     """
# ).strip()


def main():
    (N, M), Hs, *ABs = IALL(case)

    tonariDict: dict[int, int] = dict()

    for x in range(1, N + 1):
        # 空辞書はめとく
        tonariDict[x] = 0

    for a, b in ABs:
        tonariDict[a] = max(tonariDict[a], Hs[b - 1])
        tonariDict[b] = max(tonariDict[b], Hs[a - 1])

    result = 0

    for idx in range(1, N + 1):
        if Hs[idx - 1] > tonariDict[idx]:
            result += 1

    print(result)


if __name__ == "__main__":
    main()
