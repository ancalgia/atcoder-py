#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


# from textwrap import dedent

# case = dedent(
#     """
# 7
# AtCoder
# 5
# 1 4 i
# 3 0 a
# 1 5 b
# 2 0 a
# 1 4 Y
#     """
# ).strip()

# expected:
# atcYber\r


def main():
    N, S, Q, *TXCs = SL(case)

    S = list(S)

    toChangeUpper: bool | None = None

    for x in range(int(Q) - 1, -1, -1):
        if TXCs[x][0] == "3":
            TXCs[x] = "6 6 6"
            break

        if TXCs[x][0] == "2":
            TXCs[x] = "4 4 4"
            break

    pass

    for txc in TXCs:
        t, x, c = txc.split()

        t = int(t)
        x = int(x)

        if t == 1:
            if toChangeUpper == True:
                S = [x.upper() for x in S]
            elif toChangeUpper == False:
                S = [x.lower() for x in S]
            else:
                pass

            toChangeUpper = None

            S[x - 1] = c

        elif t == 4:
            toChangeUpper = False

        elif t == 6:
            toChangeUpper = True

    if toChangeUpper == True:
        S = [x.upper() for x in S]
    elif toChangeUpper == False:
        S = [x.lower() for x in S]
    else:
        pass

    print("".join(S))


if __name__ == "__main__":
    main()
