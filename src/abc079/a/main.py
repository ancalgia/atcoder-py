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
    N = int(case)

    N = str(N)

    if any(
        [
            "111" in N,
            "222" in N,
            "333" in N,
            "444" in N,
            "555" in N,
            "666" in N,
            "777" in N,
            "888" in N,
            "999" in N,
            "000" in N,
        ]
    ):
        print("Yes")

    else:
        print("No")


if __name__ == "__main__":
    main()
