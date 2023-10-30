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
    L1, L2 = SL(case)

    if L1 == ".." or L1 == "##":
        print("Yes")
        return

    if L2 == ".." or L2 == "##":
        print("Yes")
        return

    if L1 == L2:
        print("Yes")
        return

    print("No")


if __name__ == "__main__":
    main()
