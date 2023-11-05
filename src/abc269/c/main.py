#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


def convert(x: str) -> list[str]:
    pass
    if x == "0":
        return ["0"]
    else:
        return ["1", "0"]


def main():
    N = int(case)

    bitN = bin(N)[2:]

    bitlist = [convert(x) for x in bitN]

    all_patterns = itertools.product(*bitlist)

    all_pattens_10digit = [int("".join(x), 2) for x in all_patterns]

    all_pattens_10digit.sort()

    [print(x) for x in all_pattens_10digit]


if __name__ == "__main__":
    main()
