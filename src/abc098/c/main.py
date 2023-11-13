#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


# from textwrap import dedent

# case = dedent(
#     """
# 8
# WWWWWEEE
#     """
# ).strip()


def main():
    N, S = SL(case)

    N = int(N)

    dq = collections.deque(S)

    rightEast = S.count("E")
    rightWest = N - rightEast

    leftEast = 0
    leftWest = 0

    result = N * 2

    for x in range(N):
        p = dq.popleft()

        if p == "E":
            rightEast -= 1

            tmp = rightEast + leftWest
            result = min(result, tmp)

            leftEast += 1
        else:
            rightWest -= 1

            tmp = rightEast + leftWest
            result = min(result, tmp)

            leftWest += 1

    print(result)


if __name__ == "__main__":
    main()
