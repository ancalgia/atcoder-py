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
# 1 4 1 4 2
#     """
# ).strip()


def main():
    N, As = IALL(case)

    # AsSet = set(As)

    AsCounter = collections.Counter(As).most_common()

    AsCounter.sort(reverse=True)

    AnswerDict: dict[int, int] = dict()

    tmp = 0

    for x in AsCounter:
        AnswerDict[x[0]] = tmp

        tmp += x[0] * x[1]

    results = []

    for a in As:
        results.append(AnswerDict[a])

    print(*results)


if __name__ == "__main__":
    main()
