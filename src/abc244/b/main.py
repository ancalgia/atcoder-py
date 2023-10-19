#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


def turnRight(direction: int) -> int:
    return direction % 4 + 1


def main():
    N, T = SL(case)

    currDirection = 1

    currPos = [0, 0]

    for x in T:
        if x == "R":
            currDirection = turnRight(currDirection)
            continue

        match currDirection:
            case 1:
                currPos[0] += 1
            case 2:
                currPos[1] -= 1
            case 3:
                currPos[0] -= 1
            case 4:
                currPos[1] += 1

    print(f"{currPos[0]} {currPos[1]}")


if __name__ == "__main__":
    main()
