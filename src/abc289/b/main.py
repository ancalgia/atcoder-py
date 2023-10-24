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
# 1 3 4
#     """
# ).strip()
# # 2_1_5_4_3


def main():
    (N, M), As = IALL(case)

    hoge = [[x + 1, 0] for x in range(N)]

    pass

    for a in As:
        hoge[a - 1][1] = 1

    tmp: list[int] = []

    result: list[int] = []

    for x in hoge:
        if x[1] == 0:
            result.append(x[0])

            for y in tmp[::-1]:
                result.append(y)
            tmp.clear()

        else:
            tmp.append(x[0])

    print(*result)


if __name__ == "__main__":
    main()
