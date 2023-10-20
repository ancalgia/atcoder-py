#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])

# case = "12"


def main():
    N = int(case)

    yakusus = [x for x in range(1, 10) if N % x == 0]

    allNdivJs = [N // x for x in yakusus]

    zipped = list(zip(yakusus, allNdivJs))

    result = ""

    for x in range(N + 1):
        if x == 0 or x == N:
            result += str(1)
            continue

        validList = []

        for y in zipped:
            if x % y[1] == 0:
                validList.append(y[0])

        if len(validList) != 0:
            result += str(validList[0])
        else:
            result += "-"

    print(result)


if __name__ == "__main__":
    main()
