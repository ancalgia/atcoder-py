#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])

# case = "-1"


def main():
    stripped = case.rstrip()

    N = int(case)

    if len(str(abs(N))) == 1:
        if N >= 0:
            print(0)
            return
        else:
            print(-1)
            return

    if N >= 0:
        print(stripped[:-1])
        return

    else:
        if stripped[-1] == "0":
            print(stripped[:-1])
        else:
            print(int(stripped[:-1]) - 1)


if __name__ == "__main__":
    main()
