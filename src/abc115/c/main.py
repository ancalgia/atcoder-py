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
# 5
# 7
# 5
# 7
# 7
#     """
# ).strip()


def main():
    (N, K), *Hs = IALL(case)

    Hs.sort()

    Hs = [x[0] for x in Hs]

    result = 999999999999999999

    for x in range(N - K + 1):
        tmp = Hs[x + K - 1] - Hs[x]

        result = min([tmp, result])

    print(result)


if __name__ == "__main__":
    main()
