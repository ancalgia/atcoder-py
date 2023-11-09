#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


M = 998244353

case: str = "".join([x for x in sys.stdin])


# case = "2"


def updateNums(nums: list[int]) -> list[int]:
    v = []

    for x in range(len(nums)):
        if x == 0:
            v.append((nums[0] + nums[1]) % M)
            continue
        if x == len(nums) - 1:
            v.append((nums[-1] + nums[-2]) % M)
            continue

        v.append((nums[x - 1] + nums[x] + nums[x + 1]) % M)

    return v


def main():
    N = int(case)

    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1]

    for x in range(N - 1):
        nums = updateNums(nums)

    print((sum(nums)) % M)


if __name__ == "__main__":
    main()
