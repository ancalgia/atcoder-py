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
# 2 3 4 5
# 4
# 3 4 5 6
# 8
#     """
# ).strip()


def main():
    (N,), As, (M,), Bs, (X,) = IALL(case)

    stairs = [0 for x in range(X)]

    # stairs[0] = 1

    # モチを並べる
    for s in Bs:
        stairs[s - 1] = -1

    pass

    # 1歩目の処理
    for a in As:
        if (a) >= X:
            continue

        if stairs[a - 1] != -1:
            stairs[a - 1] = 1

    # stairs[0]は1段目　0段目は配列の外ということにしとく
    for idx, s in enumerate(stairs):
        if s != 1:
            continue

        for a in As:
            if (idx + a) >= X:
                continue

            if stairs[idx + a] != -1:
                stairs[idx + a] = 1

    if stairs[-1]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
