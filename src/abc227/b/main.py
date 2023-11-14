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
# 5
# 666 777 888 777 666
#     """
# ).strip()  # 3


def main():
    (N,), Ss = IALL(case)

    ableSet: set[int] = set()

    for a in range(1, 1001):
        for b in range(1, 1000):
            tmp = (4 * a * b) + (3 * a) + (3 * b)

            if tmp > 1000:
                break

            ableSet.add(tmp)

    result = 0

    for s in Ss:
        if s not in ableSet:
            result += 1

    print(result)
    pass


if __name__ == "__main__":
    main()
