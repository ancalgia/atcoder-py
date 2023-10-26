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
    (N, X), As = IALL(case)

    secret_friends = set()

    next_friend = X

    while True:
        if next_friend in secret_friends:
            print(len(secret_friends))
            return

        secret_friends.add(next_friend)

        next_friend = As[next_friend - 1]


if __name__ == "__main__":
    main()
