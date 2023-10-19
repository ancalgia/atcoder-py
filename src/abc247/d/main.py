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
    (N,), *Qs = IALL(case)

    tutu: collections.deque[int] = collections.deque()

    for q in Qs:
        if q[0] == 1:
            tutu.extendleft([q[1]] * q[2])
        else:
            pass
            ballSum = sum([tutu.pop() for x in range(q[1])])
            print(ballSum)


if __name__ == "__main__":
    main()
