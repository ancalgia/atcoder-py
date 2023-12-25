#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])

# case = "321"


def main():
    K = int(case)

    numbers: set[int] = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

    while True:
        tmp: set[int] = set([])

        for n in numbers:
            lastnum = int(str(n)[-1])

            for x in range(lastnum - 1, -1, -1):
                tmp.add(n * 10 + x)

        numbers.update(tmp.copy())

        if len(numbers) >= K:
            break

    print(sorted(numbers)[K - 1])


if __name__ == "__main__":
    main()
