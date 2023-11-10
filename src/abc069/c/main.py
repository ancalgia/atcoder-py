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
# 6
# 2 7 1 8 2 8
#     """
# ).strip()


def main():
    (N,), As = IALL(case)

    simpleAs: list[int] = []

    for x in As:
        # if x == 0:
        #     print("No")
        #     return
        if x % 4 == 0:
            simpleAs.append(4)
        elif x % 2 == 0:
            simpleAs.append(2)
        else:
            simpleAs.append(1)

    exists2 = simpleAs.count(2) > 0

    if exists2:
        print("Yes") if simpleAs.count(4) >= simpleAs.count(1) else print("No")

    else:
        print("Yes") if simpleAs.count(4) >= simpleAs.count(1) - 1 else print("No")

    pass


if __name__ == "__main__":
    main()
