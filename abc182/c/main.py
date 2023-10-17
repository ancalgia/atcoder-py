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
    S = case.rstrip()

    intList = map(int, list(S))

    parsedList = [x % 3 for x in intList]

    rest = sum(parsedList) % 3

    if rest == 0:
        print(0)
        return

    counter = collections.Counter(parsedList)

    if rest == 1:
        if 1 in counter and len(S) >= 2:
            print(1)
            return
        elif counter[2] >= 2 and len(S) >= 3:
            print(2)
            return
        else:
            print(-1)
            return

    else:
        if 2 in counter and len(S) >= 2:
            print(1)
            return
        elif counter[1] >= 2 and len(S) >= 3:
            print(2)
            return
        else:
            print(-1)
            return


if __name__ == "__main__":
    main()
