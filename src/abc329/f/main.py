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
# 6 5
# 1 1 1 2 2 3
# 1 2
# 6 4
# 5 1
# 3 6
# 4 6
#     """
# ).strip()


def main():
    (N, Q), Cs, *Queries = IALL(case)

    # Cs = [0] + Cs

    CsDict: dict[int, set[int]] = dict()

    # [CsDict.update(idx, set([x])) for idx, x in enumerate(Cs, 1)]

    for idx, x in enumerate(Cs, 1):
        CsDict[idx] = set([x])

    pass

    for a, b in Queries:
        # tmp = Cs[a].()

        # Cs[b].add(tmp)
        CsDict[b].update(CsDict[a])

        CsDict[a].clear()

        print(len(CsDict[b]))


if __name__ == "__main__":
    main()
