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
# 4 2
# abi
# aef
# bc
# acg
#     """
# ).strip()


def main():
    NK, *Ss = SL(case)

    N, K = IL(NK)

    allPtn = list(itertools.product(*[[True, False] for x in range(N)]))

    SsSets: list[list[str]] = [list(set(x)) for x in Ss]

    maxCount = 0

    for ptn in allPtn:
        tmpSets = [x for p, x in zip(ptn, SsSets) if p == True]

        counter = collections.Counter(itertools.chain.from_iterable(tmpSets))

        tmpCount = len([x for x in counter if counter[x] == K])

        maxCount = max([maxCount, tmpCount])

    print(maxCount)


if __name__ == "__main__":
    main()
