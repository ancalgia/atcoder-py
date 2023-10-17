#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])

# case = "1 1 1000"


def main():
    A, B, W = IL(case)

    W = W * 1000

    maybeMany = W // A

    maybeFew = math.ceil(W / B)

    if maybeFew > maybeMany:
        print("UNSATISFIABLE")
        return

    enables: list[int] = []

    for x in range(maybeFew, maybeMany + 1):
        if A * x <= W <= B * x:
            enables.append(x)

    if len(enables) == 0:
        print("UNSATISFIABLE")
        return

    print(f"{min(enables)} {max(enables)}")


if __name__ == "__main__":
    main()
