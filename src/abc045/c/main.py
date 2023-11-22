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

    allPtn = list(itertools.product(*[[True, False] for x in range(len(S) - 1)]))

    result = 0

    for ptn in allPtn:
        tmp = 0

        currPtn = list(ptn) + [False]

        currStr = ""

        for c, op in zip(S, currPtn):
            currStr += c
            if op:
                currStr += "+"

        result += sum(map(int, currStr.split("+")))

    print(result)


if __name__ == "__main__":
    main()
