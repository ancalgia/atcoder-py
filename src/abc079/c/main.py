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
    ABCD, *_ = SL(case)

    A, B, C, D = map(int, ABCD)

    allPtn = list(itertools.product(["+", "-"], ["+", "-"], ["+", "-"]))

    for op1, op2, op3 in allPtn:
        result = A

        result += B if op1 == "+" else -B
        result += C if op2 == "+" else -C
        result += D if op3 == "+" else -D

        if result == 7:
            print(f"{A}{op1}{B}{op2}{C}{op3}{D}=7")
            return


if __name__ == "__main__":
    main()
