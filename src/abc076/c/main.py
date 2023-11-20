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

    for x in range(len(S) - len(T), -1, -1):
        isSame = True
        for enigma, key in zip(S[x : x + len(T)], T):
            if enigma != "?" and enigma != key:
                isSame = False
                break

        if isSame:
            result = S[:x] + T + S[x + len(T) :]
            print(result.replace("?", "a"))
            return

    print("UNRESTORABLE")

    pass


if __name__ == "__main__":
    main()
