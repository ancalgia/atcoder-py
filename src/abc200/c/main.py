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
# 8
# 199 100 200 400 300 500 600 200
#     """
# ).strip()


def mod200(x: int) -> int:
    return x % 200


def main():
    (N,), As = IALL(case)

    mod200As = map(mod200, As)

    counter = collections.Counter(mod200As)

    result = 0
    for x in counter:
        result += (counter[x] * (counter[x] - 1)) // 2

    print(result)


if __name__ == "__main__":
    main()
