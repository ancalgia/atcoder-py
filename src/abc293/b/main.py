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
    (N,), Xs = IALL(case)

    called: set[int] = set()

    for n in range(1, N + 1):
        if n not in called:
            called.add(Xs[n - 1])

    unCalled: list[int] = []
    for x in range(1, N + 1):
        if x not in called:
            unCalled.append(x)

    print(len(unCalled))
    print(*unCalled)


if __name__ == "__main__":
    main()
