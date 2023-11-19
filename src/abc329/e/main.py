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
# 8888
#     """
# ).strip()


def main():
    NM, S, T = SL(case)

    N, M = IL(NM)

    if sorted(set(list(S))) != sorted(set(list(T))):
        print("No")
        return

    # for idx ,(c1,c2) in enumerate (zip(T,T[::-1])):

    for x in range(M):
        if S[x] not in T[: x + 1]:
            print("No")
            return

        if S[(x * -1) - 1] not in T[(x * -1) - 1 :]:
            print("No")
            return

    # if S[0] != T[0]:
    #     print("No")
    #     return

    # if S[-1] != T[-1]:
    #     print("No")
    #     return

    Tchars = list(T)

    Tinners = Tchars[1:-1]

    # print(Tinners)

    combs = itertools.combinations_with_replacement(Tinners, 2)

    filteredCombs = [x for x in combs if "".join(x) not in T]

    for x in filteredCombs:
        if "".join(x) in S:
            print("No")
            return

    print("Yes")


if __name__ == "__main__":
    main()
