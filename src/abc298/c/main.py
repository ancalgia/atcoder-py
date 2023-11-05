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
# 5
# 8
# 1 1 1
# 1 2 4
# 1 1 4
# 2 4
# 1 1 4
# 2 4
# 3 1
# 3 2
#     """
# ).strip()


def main():
    (N,), (Q,), *Queries = IALL(case)

    Boxes: list[list[int]] = [[] for x in range(N + 1)]

    CardsDict: dict[int, set[int]] = dict()

    for b in Boxes:
        heapq.heapify(b)

    for x in Queries:
        if x[0] == 1:
            Boxes[x[2]].append(x[1])

            if x[1] not in CardsDict:
                CardsDict[x[1]] = {x[2]}

            else:
                CardsDict[x[1]].add(x[2])

        elif x[0] == 2:
            print(*sorted(Boxes[x[1]]))

        else:
            print(*sorted(CardsDict[x[1]]))


if __name__ == "__main__":
    main()
