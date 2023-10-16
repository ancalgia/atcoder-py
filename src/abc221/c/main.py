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
    N = case

    sortedNums = sorted([*N], reverse=True)

    left: list[str] = []
    right: list[str] = []

    for idx, x in enumerate(sortedNums):
        if idx == 0:
            left.append(x)
            continue

        if len(left) < len(right):
            left.append(x)
            continue
        elif len(left) > len(right):
            right.append(x)
            continue

        else:
            if left > right:
                right.append(x)
                continue
            else:
                left.append(x)
                continue

    leftNum = int("".join(left))
    rightNum = int("".join(right))

    print(leftNum * rightNum)


if __name__ == "__main__":
    main()
