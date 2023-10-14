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
# 5 ababc
# ababc
# babc
# abacbc
# abdbc
# abbac
#     """
# ).strip()


def main():
    NT, *Ss = SL(case)

    N, T = NT.split()

    Tcounter = collections.Counter(T)

    TKeys = [x for x in Tcounter.keys()]

    results: list[int] = []

    for idx, s in enumerate(Ss):
        pass
        isF = False

        if s == T:
            results.append(idx + 1)
            continue

        s_minus_t = len(s) - len(T)

        if abs(s_minus_t) >= 2:
            # ２もじずれることはないはず
            continue

        Scounter = collections.Counter(s)

        Skeys = [x for x in Scounter.keys()]
        Strs = set(TKeys + Skeys)

        changeStrs: list[str] = []

        for sc in Strs:
            diff = abs((Scounter.get(sc) or 0) - (Tcounter.get(sc) or 0))
            if diff == 0:
                continue
            elif diff == 1:
                changeStrs.append(sc)
            else:
                isF = True
                continue

        if isF:
            continue

        if len(changeStrs) > 2:
            continue

        changeStrs.append("")
        changeStrs.append("")

        if s.replace(
            changeStrs[0],
            "",
        ).replace(
            changeStrs[1],
            "",
        ) == T.replace(
            changeStrs[0],
            "",
        ).replace(changeStrs[1], ""):
            results.append(idx + 1)
            continue

    print(len(results))

    if len(results) == 0:
        print("")
    else:
        print(" ".join(map(str, results)))


if __name__ == "__main__":
    main()
