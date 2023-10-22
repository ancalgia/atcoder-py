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
# 3 1 4 1 5
# 6
# 3 2
# 2 3 4
# 3 3
# 1 1
# 2 3 4
# 3 3
#     """
# ).strip()


def main():
    (N,), As, (Q,), *Queries = IALL(case)

    # dq: collections.deque[list[int]] = collections.deque()

    # dq.append([1] + As)

    current = As

    addList = []

    addDict: dict[int, int] = dict()

    for x in Queries:
        if x[0] == 1:
            # dq.clear()
            # dq.append([1] + ([x[1]] * N))
            current = [x[1]] * N
            # addList.clear()
            addDict.clear()
        elif x[0] == 2:
            addList.append([x[1], x[2]])

            if x[1] in addDict:
                addDict[x[1]] += x[2]
            else:
                addDict[x[1]] = x[2]

        else:
            # tgt = list(dq.copy())

            # printTgtIndex = x[1]

            # curr = tgt[0][printTgtIndex + 1 - 1]

            # for y in tgt[1:]:
            #     if y[1] == printTgtIndex:
            #         curr += y[2]

            # counter = collections.Counter(addList)
            # addCount = sum([y[1] for y in addList if y[0] == x[1]])

            print(current[x[1] - 1] + addDict.get(x[1], 0))

    pass


if __name__ == "__main__":
    main()
