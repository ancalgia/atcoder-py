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
    A, B, C = SL(case)

    dqA = collections.deque(list(A))
    dqB = collections.deque(list(B))
    dqC = collections.deque(list(C))

    next = "a"

    while True:
        if next == "a":
            if len(dqA) == 0:
                print("A")
                return
            next = dqA.popleft()
        elif next == "b":
            if len(dqB) == 0:
                print("B")
                return
            next = dqB.popleft()
        else:
            if len(dqC) == 0:
                print("C")
                return
            next = dqC.popleft()


if __name__ == "__main__":
    main()
