#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


# case = "435"


def main():
    (S,) = SL(case)

    if len(S) == 1:
        print("Yes") if S == "8" else print("No")
        return

    if len(S) == 2:
        print("Yes") if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0 else print("No")
        return

    SCounter: collections.Counter[str] = collections.Counter(S)

    oddCnt = sum([SCounter[x] for x in SCounter if int(x) % 2 == 1])
    evenCnt = sum([SCounter[x] for x in SCounter if int(x) % 2 == 0])

    if evenCnt == 0:
        print("No")
        return

    need2Even = ["16", "32", "56", "72", "96"]
    need3Even = ["24", "48", "64"]

    need2Odd = ["12", "36", "52", "76", "92"]
    need1Odd = ["28", "68", "84"]

    if SCounter["8"] >= 2 and evenCnt >= 3:
        print("Yes")
        return

    if SCounter["4"] >= 2 and oddCnt >= 1:
        print("Yes")
        return

    for x in need2Even:
        if all(
            [
                SCounter[x[0]] >= 1,
                SCounter[x[1]] >= 1,
                evenCnt >= 2,
            ]
        ):
            print("Yes")
            return

    for x in need3Even:
        if all(
            [
                SCounter[x[0]] >= 1,
                SCounter[x[1]] >= 1,
                evenCnt >= 3,
            ]
        ):
            print("Yes")
            return

    for x in need2Odd:
        if all(
            [
                SCounter[x[0]] >= 1,
                SCounter[x[1]] >= 1,
                oddCnt >= 2,
            ]
        ):
            print("Yes")
            return

    for x in need1Odd:
        if all(
            [
                SCounter[x[0]] >= 1,
                SCounter[x[1]] >= 1,
                oddCnt >= 1,
            ]
        ):
            print("Yes")
            return

    print("No")


if __name__ == "__main__":
    main()
