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
# 4 1 5
# 3 10 100
#     """
# ).strip()


def main():
    (N,), Ss, Ts = IALL(case)

    table = Ts.copy()

    while True:
        isChanged = False

        for idx in range(N):
            if table[idx] > table[idx - 1] + Ss[idx - 1]:
                table[idx] = table[idx - 1] + Ss[idx - 1]
                isChanged = True

        if not isChanged:
            [print(x) for x in table]
            return


if __name__ == "__main__":
    main()
