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
# 1 1 1 1
# 3
# 1 2
# 2 1
# 3 5
#     """
# ).strip()


def main():
    (N,), As, (Q,), *BCs = IALL(case)

    # AsCounter = list([x for x in collections.Counter(As)])
    # AsCounterXXXX = [list(x) for x in collections.Counter(As).most_common()]
    AsCounter = collections.Counter(As)

    # currentSummary = AsCounter.total()
    currentSummary = sum([AsCounter[x] * x for x in AsCounter])

    for before, after in BCs:
        currentSummary -= AsCounter[before] * before
        currentSummary += AsCounter[before] * after

        AsCounter[after] += AsCounter[before]
        AsCounter[before] = 0

        print(currentSummary)

    # pass

    # AsSet = set(As)
    # AsDict: dict[int, int] = dict()

    # for x in AsSet:
    #     AsDict[x] = x

    # currentResult = sum([AsDict[piyo[0]] * piyo[1] for piyo in AsCounter])

    # for x in BCs:
    #     currchangeCount = 0

    #     # hoge = "a" in AsDict.
    #     if x[0] in AsSet:
    #         for key in AsDict:
    #             if AsDict[key] == x[0]:
    #                 AsDict[key] = x[1]
    #                 currchangeCount += sum([z[1] for z in AsCounter if z[0] == key])

    #         AsSet.remove(x[0])
    #         AsSet.add(x[1])

    #     currentResult += (x[1] - x[0]) * currchangeCount

    #     print(currentResult)

    # # for x in range(Q):
    # #     pass

    # #     query = BCs[x]

    # #     # for y in AsCounter:
    # #     for idx in range(len(AsCounter)):
    # #         # if y[0] == query[0]:
    # #         if AsCounter[idx][0] == query[0]:
    # #             AsCounter[idx][0] = query[1]

    # #     result = sum([x[0] * x[1] for x in AsCounter])

    # #     print(result)


if __name__ == "__main__":
    main()
