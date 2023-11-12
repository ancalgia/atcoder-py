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
# 5 3
# 3 4 1 3 4
#     """
# ).strip()


def main():
    (N, K), As = IALL(case)

    separatedAs: dict[int, list[int]] = dict()

    for idx, x in enumerate(As):
        key = idx % K

        if key not in separatedAs:
            separatedAs[key] = [x]
        else:
            separatedAs[key].append(x)

    goal = sorted(As)

    separatedGoal: dict[int, list[int]] = dict()

    for idx, x in enumerate(goal):
        key = idx % K

        if key not in separatedGoal:
            separatedGoal[key] = [x]
        else:
            separatedGoal[key].append(x)

    for x in range(K):
        if sorted(separatedAs[x]) != sorted(separatedGoal[x]):
            print("No")
            return

    print("Yes")


if __name__ == "__main__":
    main()
