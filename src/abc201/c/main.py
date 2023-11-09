#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


# case = "xxxxx?xxxo"  # 15


def main():
    S, *_ = SL(case)

    if S.count("o") >= 5 or S.count("x") == 10:
        print(0)
        return

    maybeList = [str(idx) for idx, x in enumerate(S) if x == "?"]
    certainList = [str(idx) for idx, x in enumerate(S) if x == "o"]

    allPtn = itertools.product(
        maybeList + certainList, maybeList + certainList, maybeList + certainList, maybeList + certainList
    )

    result = 0

    for ptn in allPtn:
        isValid = True
        for certain in certainList:
            if certain not in ptn:
                isValid = False
                break

        if isValid:
            result += 1

    print(result)


if __name__ == "__main__":
    main()
