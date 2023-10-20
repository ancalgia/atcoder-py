#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])

# case = "0 0 3 3"


def main():
    X1, X2, X3, X4 = IL(case)

    steps = [[1, 2], [1, -2], [2, 1], [2, -1], [-1, 2], [-1, -2], [-2, 1], [-2, -1]]

    for x in steps:
        step1 = [X1 + x[0], X2 + x[1]]

        for y in steps:
            step2 = [step1[0] + y[0], step1[1] + y[1]]

            if step2[0] == X3 and step2[1] == X4:
                print("Yes")
                return

    print("No")


if __name__ == "__main__":
    main()
