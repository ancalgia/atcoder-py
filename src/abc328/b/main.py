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
# 12
# 31 29 31 30 31 30 31 31 30 31 30 31
#     """
# ).strip()

# from textwrap import dedent

# case = dedent(
#     """
# 1
# 1
#     """
# ).strip()


def main():
    (N,), Ds = IALL(case)

    result = 0

    for idx, x in enumerate(Ds, 1):
        for y in range(1, x + 1):
            tmpSet = set(str(idx) + str(y))

            if len(tmpSet) == 1:
                result += 1

    print(result)


if __name__ == "__main__":
    main()
