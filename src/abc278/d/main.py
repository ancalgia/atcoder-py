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
# 10
# 1 8 4 15 7 5 7 5 8 0
# 20
# 2 7 0
# 3 7
# 3 8
# 1 7
# 3 3
# 2 4 4
# 2 4 9
# 2 10 5
# 1 10
# 2 4 2
# 1 10
# 2 3 1
# 2 8 11
# 2 3 14
# 2 1 9
# 3 8
# 3 8
# 3 1
# 2 6 5
# 3 7
#     """
# ).strip()


def main():
    (N,), As, (Q,), *Queries = IALL(case)

    # dq: collections.deque[list[int]] = collections.deque()

    # dq.append([1] + As)

    current = 0

    # addList = []

    addDict: dict[int, int] = dict()

    for idx, x in enumerate(As, 1):
        addDict[idx] = x

    # currentValue = 0

    for x in Queries:
        if x[0] == 1:
            # dq.clear()
            # dq.append([1] + ([x[1]] * N))
            current = x[1]
            # addList.clear()
            addDict.clear()
        elif x[0] == 2:
            # addList.append([x[1], x[2]])

            # if x[1] in addDict:
            #     addDict[x[1]] += x[2]
            # else:
            #     addDict[x[1]] = x[2]

            addDict.setdefault(x[1], 0)
            addDict[x[1]] += x[2]

            # if x[1] in addDict:
            #     addDict[x[1]] += x[2]
            # else:
            #     addDict[x[1]] = x[2]

        else:
            pass

            # tgt = list(dq.copy())

            # printTgtIndex = x[1]

            # curr = tgt[0][printTgtIndex + 1 - 1]

            # for y in tgt[1:]:
            #     if y[1] == printTgtIndex:
            #         curr += y[2]

            # counter = collections.Counter(addList)
            # addCount = sum([y[1] for y in addList if y[0] == x[1]])

            # current = [z + addDict.get(idx, 0) for idx, z in enumerate(current, 1)]

            # # print(current[x[1] - 1] + addDict.get(x[1], 0))
            # print(current[x[1] - 1])
            # current[x[1] - 1] += addDict.get(x[1], 0)
            # addDict[x[1]] = 0

            # print(current[x[1] - 1] + addDict.get(x[1], 0))
            print(current + addDict.get(x[1], 0))

            # addDict.clear()

    pass


if __name__ == "__main__":
    main()
