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
    (N,), As = [list(map(int, x.split())) for x in case.splitlines()]

    kakudos = [0]

    current_kakudo = 0

    for x in As:
        current_kakudo = (current_kakudo + x) % 360

        kakudos.append(current_kakudo)

    kakudos.sort()
    kakudos.append(360)

    print(max([r - l for l, r in zip(kakudos, kakudos[1:])]))


if __name__ == "__main__":
    main()
