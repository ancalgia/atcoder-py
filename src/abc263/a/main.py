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
    ABCDE = IL(case)

    cardCounter = collections.Counter(ABCDE)

    if len(cardCounter) != 2:
        print("No")
        return

    print("Yes") if cardCounter.most_common()[0][1] in [2, 3] else print("No")


if __name__ == "__main__":
    main()
