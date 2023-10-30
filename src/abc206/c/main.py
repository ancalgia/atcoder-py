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
# 3
# 1 7 1
#     """
# ).strip()


def main():
    (N,), As = IALL(case)

    AsCounter = collections.Counter(As)

    # AsCountList = AsCounter.most_common()

    # AsCountList.sort()

    # counterLen = len(AsCountList)

    result = 0

    ttl = AsCounter.total()

    # for x in range(counterLen):
    #     for y in range(x + 1, counterLen):
    #         result += AsCountList[x][1] * AsCountList[y][1]

    for x in AsCounter:
        result += AsCounter[x] * (ttl - AsCounter[x])

    print(result // 2)


if __name__ == "__main__":
    main()
