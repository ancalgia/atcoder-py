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
    N, *Ss = SL(case)
    N = int(N)

    Mcount = len([x for x in Ss if x[0] == "M"])
    Acount = len([x for x in Ss if x[0] == "A"])
    Rcount = len([x for x in Ss if x[0] == "R"])
    Ccount = len([x for x in Ss if x[0] == "C"])
    Hcount = len([x for x in Ss if x[0] == "H"])

    ables = [x for x in [Mcount, Acount, Rcount, Ccount, Hcount] if x != 0]

    if len(ables) <= 2:
        print(0)
        return

    ablePtn = itertools.combinations(ables, 3)
    result = 0

    for ptn in ablePtn:
        result += ptn[0] * ptn[1] * ptn[2]

    print(result)


if __name__ == "__main__":
    main()
