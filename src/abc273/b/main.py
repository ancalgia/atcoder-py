#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


# case = "2048 2"  # 2100
# case = "999 3"  # 1000
# case = "1 15"  # 0

# case = "314159265358979 12"  # 314000000000000


def main():
    X, K = IL(case)

    X = list(map(int, list(str(X))))

    pass

    for pos in range(1, K + 1):
        if pos == len(X):
            X[-pos] = 10 if X[-pos] in [5, 6, 7, 8, 9, 10] else 0
            continue

        if pos > len(X):
            X[0] = 0
            break

        if X[-pos] in [5, 6, 7, 8, 9, 10]:
            X[-pos - 1] += 1

        X[-pos] = 0

    for pos in range(1, len(X)):
        if X[-pos] == 10:
            X[-pos - 1] += 1
            X[-pos] = 0

    print(int("".join([str(x) for x in X])))


if __name__ == "__main__":
    main()
