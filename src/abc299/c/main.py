#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


def countDango(maybeDango: str, isBar: bool) -> int:
    pass

    word = "o" if isBar else "-"

    if maybeDango[1:] == word * (len(maybeDango) - 1):
        return len(maybeDango) - 1
    else:
        return -1


def main():
    N, S = SL(case)

    N = int(N)

    # dango = -1

    # start = 0
    # stop = 1

    # while True:
    #     if stop >= len(S):
    #         print(dango)
    #         return

    #     isStartBar = S[start] == "-"

    #     level = countDango(S[start:stop], isStartBar)

    #     if level != -1:
    #         dango = max([dango, level])
    #         stop += 1
    #     else:
    #         start += 1

    #         stop = max([start + 2, stop])

    oCount = S.count("o")
    barCount = S.count("-")

    if oCount == 0 or barCount == 0:
        print(-1)
        return

    minimum = 0
    maximum = oCount

    result: int = -1

    while True:
        if minimum == maximum:
            if S.find("o" * minimum) != -1:
                result = max([result, minimum])

            print(result)
            return

        tgt = (minimum + maximum) // 2

        if S.find("o" * tgt) != -1:
            result = max([result, tgt])

            if abs(minimum - maximum) < 2:
                minimum += 1
            else:
                minimum = tgt
        else:
            if abs(minimum - maximum) < 2:
                minimum ^= 1
            else:
                maximum = tgt


if __name__ == "__main__":
    main()
