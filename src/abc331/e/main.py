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
# 2 1 0
# 1000000000 1
# 1000000000
#     """
# ).strip()


def main():
    (N, M, L), As, Bs, *CDs = IALL(case)

    NGDict: dict[int, set[int]] = dict()

    for c, d in CDs:
        if c in NGDict:
            NGDict[c].add(d)
        else:
            NGDict[c] = {d}
        if d in NGDict:
            NGDict[d].add(c)
        else:
            NGDict[d] = {c}

    # allPtn = list(itertools.product(range(1, N + 1), range(1, M + 1)))

    maxResult = 0

    for x in range(1, N + 1):
        tmp = max(
            [Bs[y - 1] for y in [z for z in range(1, M + 1) if x not in NGDict or z not in NGDict[x]]] + [0],
        )
        maxResult = max(maxResult, As[x - 1] + tmp)

    # for x, y in allPtn:
    #     if y not in NGDict:
    #         maxResult = max(maxResult, As[x - 1] + Bs[y - 1])
    #     elif x not in NGDict[y]:
    #         maxResult = max(maxResult, As[x - 1] + Bs[y - 1])

    print(maxResult)


if __name__ == "__main__":
    main()
