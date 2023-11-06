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
    A1s, A2s, A3s, (N,), *Bs = IALL(case)

    Bs = [x[0] for x in Bs]

    # if any([all([A1s[0]in Bs,A1s[1]in Bs,,A1s[2]in Bs])]):1

    if any(
        [
            all([A1s[0] in Bs, A1s[1] in Bs, A1s[2] in Bs]),
            all([A2s[0] in Bs, A2s[1] in Bs, A2s[2] in Bs]),
            all([A3s[0] in Bs, A3s[1] in Bs, A3s[2] in Bs]),
            all([A1s[0] in Bs, A2s[0] in Bs, A3s[0] in Bs]),
            all([A1s[1] in Bs, A2s[1] in Bs, A3s[1] in Bs]),
            all([A1s[2] in Bs, A2s[2] in Bs, A3s[2] in Bs]),
            all([A1s[0] in Bs, A2s[1] in Bs, A3s[2] in Bs]),
            all([A3s[0] in Bs, A2s[1] in Bs, A1s[2] in Bs]),
        ]
    ):
        print("Yes")
        return

    print("No")


if __name__ == "__main__":
    main()
