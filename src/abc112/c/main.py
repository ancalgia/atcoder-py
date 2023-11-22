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
# 59 3 0
# 64 94 56
# 5 62 11
# 3 93 14
#     """
# ).strip()
# # 55 80 79


def main():
    (N,), *XYHs = IALL(case)

    XYHs = [(x[0], x[1], x[2]) for x in XYHs]

    for x in range(101):
        for y in range(101):
            distances = []
            distances0 = []

            for zx, zy, zh in XYHs:
                if zh != 0:
                    distances.append(abs(x - zx) + abs(y - zy) + zh)
                else:
                    distances0.append(abs(x - zx) + abs(y - zy) + zh)

            if len(set(distances)) == 1:
                if all([z >= distances[0] for z in distances0]):
                    print(*[x, y, distances[0]])
                    return


if __name__ == "__main__":
    main()
