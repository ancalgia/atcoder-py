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
# 4
# 1 4
# 2 10
# 2 8
# 3 6
#     """
# ).strip()

# ex16 res14


def main():
    (N,), *FSs = IALL(case)

    FSs.sort(key=lambda x: x[1], reverse=True)

    first = FSs[0]

    otherSecond = [0, 0]
    sameSecond = [0, 0]
    for x in FSs[1:]:
        if x[0] != first[0]:
            otherSecond = x
            break

    for x in FSs[1:]:
        if x[0] == first[0]:
            sameSecond = x
            break

    better = max([otherSecond[1], sameSecond[1] // 2])

    print(first[1] + better)


if __name__ == "__main__":
    main()
