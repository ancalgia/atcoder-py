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
# 5
# 1000000000 0
# 1000000000 0
# 1000000000 0
# 1000000000 0
# 1000000000 4 1 2 3 4
# """
# ).strip()


def main():
    (N,), *Ts = IALL(case)

    wazalist = [[idx, False] for idx in range(int(N))]

    wazalist[-1][1] = True

    next_check_set: set[int] = set([wazalist[-1][0]])

    already_checked_set: set[int] = set()

    while True:
        if already_checked_set >= next_check_set:
            break

        nextList = next_check_set.copy()

        next_check_set.clear()

        for x in nextList:
            already_checked_set.add(x)

            if Ts[x][1] != 0:
                next_check_set.update([x - 1 for x in Ts[x][2:]])

    time = 0

    for x in already_checked_set:
        time += Ts[x][0]

    print(time)


if __name__ == "__main__":
    main()
