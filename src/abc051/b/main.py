#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])

# case = "2 2"


def main():
    K, S = IL(case)

    pass

    result = 0

    for x in range(K + 1):
        if S - x > K * 2:
            continue

        for y in range(K + 1):
            if S - x - y > K:
                continue

            elif x + y > S:
                break

            else:
                result += 1

    print(result)


if __name__ == "__main__":
    main()
