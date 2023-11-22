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
# 1
# 2 1
# 1
# 1 1
# 1
# 2 0
#     """
# ).strip()


def main():
    (N,), *rest = IALL(case)

    declaresList: list[list[list[int]]] = []

    tmpDeclare: list[list[int]] = []

    for x in rest:
        if len(x) == 1:
            declaresList.append(tmpDeclare.copy())
            tmpDeclare = []
            continue

        tmpDeclare.append(x)

    declaresList.append(tmpDeclare.copy())

    declaresList = declaresList[1:]

    maxHonests = 0

    allPtn = list(itertools.product(*[[True, False] for x in range(N)]))

    for ptn in allPtn:
        isValid = True

        for manIdx in range(N):
            if ptn[manIdx] == False:
                continue

            for declare in declaresList[manIdx]:
                tgt = declare[0]
                isHonest = declare[1] == 1

                if ptn[tgt - 1] != isHonest:
                    isValid = False
                    break

            if not isValid:
                break

        if isValid:
            maxHonests = max(maxHonests, ptn.count(True))

    print(maxHonests)

    pass


if __name__ == "__main__":
    main()
