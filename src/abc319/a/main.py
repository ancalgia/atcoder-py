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
    pls = {
        "tourist": 3858,
        "ksun48": 3679,
        "Benq": 3658,
        "Um_nik": 3648,
        "apiad": 3638,
        "Stonefeang": 3630,
        "ecnerwala": 3613,
        "mnbvmar": 3555,
        "newbiedmy": 3516,
        "semiexp": 3481,
        "tourist": 3858,
        "ksun48": 3679,
        "Benq": 3658,
        "Um_nik": 3648,
        "apiad": 3638,
        "Stonefeang": 3630,
        "ecnerwala": 3613,
        "mnbvmar": 3555,
        "newbiedmy": 3516,
        "semiexp": 3481,
    }

    tgt = case.rstrip()

    print(pls[tgt])

    pass


if __name__ == "__main__":
    main()
