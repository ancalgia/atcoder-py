#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


def main():
    (N,), As = IALL(case)

    resultBoxes: dict[int, bool] = {}

    for x in range(N):
        resultBoxes[x + 1] = False

    AsWithNum = [(idx, x) for idx, x in enumerate(As, 1)]

    for x in range(N, 0, -1):
        # 対象となる箱

        tgtBox: list[bool] = []
        for y in range(x, N + 1, x):
            tgtBox.append(resultBoxes[y])

        tgtBoxesCurrent = tgtBox.count(True) % 2

        if tgtBoxesCurrent == As[x - 1]:
            continue
        else:
            resultBoxes[x] = True

    result = sorted([x for x in resultBoxes if resultBoxes[x] == True])
    print(len(result))
    if len(result):
        print(*result)


if __name__ == "__main__":
    main()
