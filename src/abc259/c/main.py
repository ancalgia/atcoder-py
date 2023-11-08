#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


def compressString(s: str) -> list[tuple[str, int]]:
    chunk: list[tuple[str, int]] = []

    lastStr = ""

    count = 0

    for c in s:
        if c != lastStr:
            if count > 0:
                chunk.append((lastStr, count))
            lastStr = c
            count = 1

        else:
            count += 1

    chunk.append((lastStr, count))

    return chunk


def main():
    S, T = SL(case)

    compS = compressString(S)
    compT = compressString(T)

    if len(compS) != len(compT):
        print("No")
        return

    for sTup, tTup in zip(compS, compT):
        if sTup[0] != tTup[0]:
            print("No")
            return

        if sTup[1] > tTup[1]:
            print("No")
            return

        if sTup[1] == 1 and tTup[1] != 1:
            print("No")
            return

    print("Yes")


if __name__ == "__main__":
    main()
