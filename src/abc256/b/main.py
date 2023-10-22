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
    (N,), As = IALL(case)

    curr_runners = []

    for x in range(N):
        move = As[x]

        if move == 1:
            curr_runners = [1] + curr_runners
        elif move == 2:
            curr_runners = [0, 1] + curr_runners
        elif move == 3:
            curr_runners = [0, 0, 1] + curr_runners
        else:
            curr_runners = [0, 0, 0, 1] + curr_runners

    score = sum([x for x in curr_runners[3:]])

    print(score)


if __name__ == "__main__":
    main()
