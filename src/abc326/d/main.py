#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


# case: str = "".join([x for x in sys.stdin])


from textwrap import dedent

case = dedent(
    """
5
ABCBC
ACAAB
    """
).strip()


def getRandomLine(n: int) -> list[tuple[str]]:
    ptn = ["A", "B", "C"] + (["."] * (n - 3))

    ho = list(set(itertools.permutations(ptn, n)))

    return list(ho)


def main():
    N, R, C = SL(case)

    N = int(N)

    lines = getRandomLine(N)

    matrixes = list(itertools.combinations(lines, N))

    for m in matrixes:
        isNG = False

        for x in range(N):
            tmp = ""
            for y in range(N):
                tgt = m[y][x]
                if tgt != ".":
                    if tgt in tmp:
                        isNG = True
                        break
                    else:
                        tmp += tgt

            if isNG:
                break
        if isNG:
            continue

        # horizon
        tmpHorStr = ""
        for hor in range(N):
            for ver in range(N):
                if m[hor][ver] != ".":
                    tmpHorStr += m[hor][ver]
                    continue

        if tmpHorStr != R:
            continue

        # ver
        tmpVerStr = ""
        for ver in range(N):
            for hor in range(N):
                if m[ver][hor] != ".":
                    tmpVerStr += m[ver][hor]
                    continue
        if tmpVerStr != R:
            continue

        print("Yes")
        for result in m:
            print("".join(result))
        return

    print("No")

    pass


if __name__ == "__main__":
    main()
