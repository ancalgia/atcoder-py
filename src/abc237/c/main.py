#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])
# case = "atcoder"


def main():
    S, *_ = case.splitlines()

    if len(S.replace("a", "")) == 0:
        print("Yes")
        return

    count = 0

    for x in range(len(S)):
        if S[-(x + 1)] == "a":
            count += 1
        else:
            break

    count2 = 0
    for x in range(len(S)):
        if S[x] == "a":
            count2 += 1
        else:
            break

    if count2 > count:
        print("No")
        return

    if count > 0:
        S = S[:-count]

    if count2 > 0:
        S = S[count2:]

    # while S.endswith("a"):
    #     S = S[0:-1]

    if S == S[::-1]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
