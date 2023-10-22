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
    S, *_ = SL(case)

    lenS = len(S)

    if lenS == 1:
        print("No")
        return

    if S != S[::-1]:
        print("No")
        return

    top = S[: int((lenS - 1) / 2)]
    end = S[int((lenS + 3) / 2) - 1 :]

    if lenS == 3:
        print("Yes")
        return

    # if top != top[::-1] or end != end[::-1]:
    if top != end:
        print("No")
        return

    print("Yes")


if __name__ == "__main__":
    main()
