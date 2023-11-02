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
    Ss = SL(case)

    Ss = list(map(list, Ss))

    pos: list[int] = []

    for x in range(8):
        for y in range(8):
            if Ss[x][y] == "*":
                pos = [x, y]

    alphaDict = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}
    numDict = {0: "8", 1: "7", 2: "6", 3: "5", 4: "4", 5: "3", 6: "2", 7: "1"}

    print(f"{alphaDict[pos[1]]}{numDict[pos[0]]}")


if __name__ == "__main__":
    main()
