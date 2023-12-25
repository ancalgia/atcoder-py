#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])

# case = "4"


def main():
    N = int(case)

    result = 0

    for a in range(1, N + 1):
        if a * a * a > N:
            break
        for b in range(a, N + 1):
            if a * b * b > N:
                break

            result += (N // (a * b)) - b + 1

    print(result)


if __name__ == "__main__":
    main()
