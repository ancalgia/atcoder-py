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
# 2 3
# GCP
# PPP
# CCC
# PPC
#     """
# ).strip()


def main():
    NM, *As = SL(case)

    N, M = IL(NM)

    usersDict: dict = dict()
    # usersList: list[tuple[int, int, list[list[str]]]] = []
    usersList: list = []

    for idx, x in enumerate(As, 1):
        te = list(x)

        # hoge = (idx, 0, [te])

        usersDict[idx] = (idx, 0, [te])

        usersList.append([0, idx, [te]])

    pass

    for m in range(M):
        for x in range(0, N * 2, 2):
            le = usersList[x][2][0][m]

            ri = usersList[x + 1][2][0][m]

            if le == ri:
                continue

            elif any(
                [
                    le == "G" and ri == "C",
                    le == "C" and ri == "P",
                    le == "P" and ri == "G",
                ]
            ):
                usersList[x][0] -= 1

            else:
                usersList[x + 1][0] -= 1

        pass
        usersList.sort()

    pass

    for x in usersList:
        print(x[1])


if __name__ == "__main__":
    main()
