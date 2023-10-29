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
# 1 2
# 1 3
# 4 5
#     """
# ).strip()


def main():
    (N, M), *UVs = IALL(case)

    allPoint = [{x} for x in range(1, N + 1)]

    for x in range(200):
        for u, v in UVs:
            for p in allPoint:
                if u in p and v not in p:
                    p.add(v)
                if v in p and u not in p:
                    p.add(u)

    resultSet = set([str(x) for x in allPoint])

    print(len(resultSet))
    pass


if __name__ == "__main__":
    main()
