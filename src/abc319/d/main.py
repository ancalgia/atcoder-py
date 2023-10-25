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
# 13 3
# 9 5 2 7 1 8 8 2 1 5 2 3 6
#     """
# ).strip()
# # 26


def main():
    (N, M), Ls = IALL(case)

    minW = max(Ls)

    maxW = sum(Ls) + N - 1

    def chk(width: int):
        lineCount = 0
        lineStrCnt = 0

        for x in Ls:
            if lineStrCnt == 0:
                # 最初だけ
                lineCount += 1
                lineStrCnt = x
                continue

            if lineStrCnt + 1 + x <= width:
                lineStrCnt += 1 + x
                continue
            else:
                lineCount += 1
                lineStrCnt = x

        return lineCount

    while True:
        if minW == maxW:
            print(minW)
            return

        tgt = (minW + maxW) // 2

        needLine = chk(tgt)

        if needLine > M:
            if abs(minW - maxW) == 1:
                minW += 1
            else:
                minW = tgt

        else:
            if abs(minW - maxW) == 1:
                maxW -= 1
            else:
                maxW = tgt


if __name__ == "__main__":
    main()
