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
# 0 1 1
# 1 0 0
# 0 1 0
# 1 1 0
# 0 0 1
# 1 1 1
#     """
# ).strip()


def main():
    (N,), *rest = IALL(case)

    rectA = rest[:N]
    rectB = rest[N:]

    set1Pos: set[tuple[int, int]] = set()

    for x in range(N):
        for y in range(N):
            if rectB[x][y] == 1:
                set1Pos.add((x, y))

    pass

    for _ in range(4):
        isSatisfied = True
        for ax in range(N):
            for ay in range(N):
                if rectA[ax][ay] == 1 and (ax, ay) not in set1Pos:
                    isSatisfied = False
                    break
            if not isSatisfied:
                break

        if isSatisfied:
            print("Yes")
            return

        rectA: list[list[int]] = list(zip(*rectA[::-1]))

    print("No")


if __name__ == "__main__":
    main()
