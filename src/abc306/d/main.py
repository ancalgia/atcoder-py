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
# 5
# 1 100
# 1 300
# 0 -200
# 1 500
# 1 300
#     """
# ).strip()


def main():
    (N,), *XYs = IALL(case)

    fileteredXYs = [(x[0], x[1]) for x in XYs if (x[0] == 0 or x[1] > 0)]

    pass

    chunks: list[list[tuple[int, int]]] = []
    tmp: list[tuple[int, int]] = []
    current = fileteredXYs[0][0]

    pass

    for x in fileteredXYs:
        if current == 0 and x[0] == 1:
            chunks.append(tmp.copy())
            tmp.clear()
            tmp.append(x)
        else:
            tmp.append(x)

        current = x[0]

    if len(tmp) != 0:
        chunks.append(tmp.copy())

    result = 0

    for ch in chunks:
        bestPoison = max([x[1] for x in ch if x[0] == 1] + [0])

        medicines = [x[1] for x in ch if x[0] == 0]

        if len(medicines) == 0:
            result += bestPoison
            continue

        bestMedicine = max(medicines) if all([x <= 0 for x in medicines]) else sum([x for x in medicines if x >= 0])

        if bestPoison + bestMedicine > 0:
            result += bestPoison + bestMedicine

    print(result)

    pass


if __name__ == "__main__":
    main()
