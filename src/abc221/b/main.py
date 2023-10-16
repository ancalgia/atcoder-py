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
    S, T = SL(case)

    cnt: list[int] = []

    diffstr: list[str] = []

    for idx, x in enumerate(zip(S, T)):
        if x[0] != x[1]:
            cnt.append(idx)
            diffstr.append(x[0] + x[1])

    if len(cnt) == 0:
        print("Yes")
        return

    if len(cnt) == 2 and abs(cnt[0] - cnt[1]) == 1:
        if diffstr[0] == diffstr[1][::-1]:
            print("Yes")
        else:
            print("No")

    else:
        print("No")


if __name__ == "__main__":
    main()
