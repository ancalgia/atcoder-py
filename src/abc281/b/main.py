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

    if len(S) != 8:
        print("No")
        return

    if S[0] == S[0].lower():
        print("No")
        return

    if S[1:-1] != S[1:-1].lower():
        print("No")
        return

    if S[1] == "0":
        print("No")
        return

    if S[-1] == S[-1].lower():
        print("No")
        return

    print("Yes")


if __name__ == "__main__":
    main()
