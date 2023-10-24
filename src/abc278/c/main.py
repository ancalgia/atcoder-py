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
# 3 9
# 1 1 2
# 3 1 2
# 1 2 1
# 3 1 2
# 1 2 3
# 1 3 2
# 3 1 3
# 2 1 2
# 3 1 2
#     """
# ).strip()


def main():
    (N, Q), *Queries = IALL(case)

    # users: list[list[set[int]]] = [[set({}), set({})] for x in range(N)]

    ffSet: set[tuple[int, int]] = set({(0, 0)})

    for x in Queries:
        ptn = x[0]

        if ptn == 1:
            ffSet.add((x[1], x[2]))
        elif ptn == 2:
            ffSet.discard((x[1], x[2]))

        else:
            pass
            if (x[1], x[2]) in ffSet and (x[2], x[1]) in ffSet:
                print("Yes")
            else:
                print("No")

    pass


if __name__ == "__main__":
    main()
