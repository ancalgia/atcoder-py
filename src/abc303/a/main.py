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
# l0w
# 1ow
#     """
# ).strip()


def main():
    N, S, T = SL(case)

    for s, t in zip(S, T):
        if any(
            [
                s == t,
                s in ["o", "0"] and t in ["o", "0"],
                s in ["1", "l"] and t in ["1", "l"],
            ]
        ):
            continue

        else:
            print("No")
            return

    print("Yes")


if __name__ == "__main__":
    main()
