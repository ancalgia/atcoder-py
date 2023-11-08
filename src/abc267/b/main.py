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
    S, *_ = SL(case)

    if S[0] == "1":
        print("No")
        return

    pass

    TFlist = [
        S[6] == "1",
        S[3] == "1",
        S[1] == "1" or S[7] == "1",
        S[4] == "1",
        S[2] == "1" or S[8] == "1",
        S[5] == "1",
        S[9] == "1",
    ]

    if TFlist.count(True) == 1:
        print("No")
        return

    TrueIndexes = [i for i, x in enumerate(TFlist) if x == True]

    diffs = [right - left for left, right in zip(TrueIndexes, TrueIndexes[1:])]

    print("Yes") if diffs.count(1) != len(diffs) else print("No")


if __name__ == "__main__":
    main()
