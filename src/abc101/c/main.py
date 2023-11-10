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
# 21 3
# 5 5 5 5 1 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
#     """
# ).strip()  # 4


# 5 5 5 5
# 1 5 5 5 5
# 5 5 5 5 5
# 5 5 5 5 5 5 5
# from textwrap import dedent

# case = dedent(
#     """
# 4 3
# 2 3 1 4
#     """
# ).strip()


def main():
    (N, K), As = IALL(case)

    minIdx = As.index(1)

    if N == K:
        print(1)
        return

    if K == 2:
        print(N - 1)
        return

    print(math.ceil((N - 1) / (K - 1)))


if __name__ == "__main__":
    main()
