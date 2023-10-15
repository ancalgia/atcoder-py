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
# 7 50
# 11 12 16 22 27 28 31
# """
# ).strip()


def main():
    (N, K), As = IALL(case)

    sums: list[int] = [0]
    tmp = 0
    for x in As:
        tmp += x
        sums.append(tmp)

    count = 0

    left = 0
    while True:
        if left > N - 1:
            print(count)
            return

        for right in range(left + 1, N + 1):
            if (sums[right] - sums[left]) <= K:
                count += 1

            else:
                break

        left += 1

    pass


if __name__ == "__main__":
    main()
