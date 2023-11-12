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
# 11 4
# mississippi
# 3 9
# 4 10
# 4 6
# 7 7
#     """
# ).strip()


def main():
    (NQ), S, *Queries = SL(case)

    sameOrDiffList = [right == left for left, right in zip(S, S[1:])]

    # print(sameOrDiffList)

    countList: list[int] = [0]

    count = 0
    for x in sameOrDiffList:
        if x:
            count += 1

        countList.append(count)

    for q in Queries:
        le, ri = IL(q)

        print(countList[ri - 1] - countList[le - 1])

    pass


if __name__ == "__main__":
    main()
