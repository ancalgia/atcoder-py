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
# 5 3
# -30 -10 10 20 50
#     """
# ).strip()


def main():
    (N, K), Xs = IALL(case)

    if 0 in Xs:
        K -= 1

    if K == 0:
        print(0)
        return

    positiveCandles = sorted([x for x in Xs if x > 0])
    negativeCandles = sorted([-x for x in Xs if x < 0])

    # 正のキャンドル数
    positiveCount = len(positiveCandles)
    negativeCount = len(negativeCandles)

    currentMin = 10**19

    for posicount, posi in enumerate(positiveCandles, 1):
        positiveWalk = posi

        if posicount == K:
            currentMin = min(currentMin, positiveWalk)
            break

        negativeNeed = K - posicount
        if negativeNeed > negativeCount:
            continue
        negativeWalk = positiveWalk + negativeCandles[negativeNeed - 1]
        currentMin = min(currentMin, positiveWalk + negativeWalk)

    for negacount, nega in enumerate(negativeCandles, 1):
        negativeWalk = nega

        if negacount == K:
            currentMin = min(currentMin, negativeWalk)
            break

        positiveNeed = K - negacount
        if positiveNeed > positiveCount:
            continue
        positiveWalk = negativeWalk + abs(positiveCandles[positiveNeed - 1])
        currentMin = min(currentMin, negativeWalk + positiveWalk)

    print(currentMin)


if __name__ == "__main__":
    main()
