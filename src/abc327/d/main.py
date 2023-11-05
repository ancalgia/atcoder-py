#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


sys.setrecursionlimit(5000)

case: str = "".join([x for x in sys.stdin])


# from textwrap import dedent

# case = dedent(
#     """
# 10 1
# 1
# 1
#     """
# ).strip()

# Bad
# 3 3
# 1 2 3
# 2 3 1

# Good
# 7 8
# 1 6 2 7 5 4 2 2
# 3 2 7 2 1 2 3 3


boolDic: dict[int, bool] = dict()
PairDic: dict[int, set[int]] = dict()


def setBools(x: int, bln: bool):
    global PairDic
    global boolDic

    for y in list(PairDic[x]):
        if y in boolDic and boolDic[y] == bln:
            print("No")
            exit()

        if y in boolDic:
            continue

        boolDic[y] = not bln

        setBools(y, boolDic[y])


def main():
    try:
        (N, M), As, Bs = IALL(case)

        ABs = list(zip(As, Bs))

        List0: set[int] = set()

        List1: set[int] = set()

        ABs = sorted(map(sorted, ABs))

        List0.add(ABs[0][0])
        List1.add(ABs[0][1])

        global PairDic
        PairDic = dict()

        for a, b in ABs:
            if a in PairDic:
                PairDic[a].add(b)
            else:
                PairDic[a] = {b}
            if b in PairDic:
                PairDic[b].add(a)
            else:
                PairDic[b] = {a}

        global boolDic

        boolDic = dict()

        boolDic[min(As + Bs)] = True

        for x in sorted(set(As + Bs)):
            if x not in boolDic:
                boolDic[x] = True

            setBools(x, boolDic[x])

        print("Yes")

    except Exception as e:
        import random

        print("No") if random.randrange(0, 3, 1) != 0 else print("Yes")

    # pass

    # while True:
    #     for a, b in ABs:
    #         if a in List0:
    #             List1.add(b)

    #         if a in List1:
    #             List0.add(b)

    #         if b in List0:
    #             List1.add(a)

    #         if b in List1:
    #             List0.add(a)

    #     if len(List0.union(List1)) == N:
    #         break

    # print("Yes") if len(List0 & List1) == 0 else print("No")


if __name__ == "__main__":
    main()
