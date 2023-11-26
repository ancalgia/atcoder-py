#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


# case = "RRRLLRLLRRRLLLLL"


def main():
    S, *_ = SL(case)

    result: list[int] = []

    splittedSList = S.replace("LR", "L|R").split("|")

    for spS in splittedSList:
        count = len(spS)
        rlIdx = spS.find("RL")

        tmpResult = [0 for x in range(count)]

        tmpResult[rlIdx] = count // 2
        tmpResult[rlIdx + 1] = count // 2

        if count % 2 == 1:
            if rlIdx % 2 == 0:
                tmpResult[rlIdx] += 1
            else:
                tmpResult[rlIdx + 1] += 1

        result.extend(tmpResult.copy())

        # print(rlIdx)

    print(*result)

    # for idx in range(len(S)):
    #     1

    pass


if __name__ == "__main__":
    main()
