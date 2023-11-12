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
# 5 6
# 1 5
# 4 5
# 2 3
# 1 4
# 3 5
# 2 5
#     """
# ).strip()


def main():
    (N, M), *UVs = IALL(case)

    PointDict: dict[int, list[int]] = dict()

    for u, v in UVs:
        if u not in PointDict:
            PointDict[u] = [v]
        else:
            PointDict[u].append(v)
        if v not in PointDict:
            PointDict[v] = [u]
        else:
            PointDict[v].append(u)

    result: set[tuple[int, int, int]] = set()

    for x in range(1, N + 1):
        # Xは1つ目の頂点

        if x not in PointDict:
            continue
        hoge = PointDict[x]
        # print(hoge)

        for y in hoge:
            # Yは2つ目の頂点

            piyo = PointDict[y]

            for z in piyo:
                if z in hoge:
                    result.add(tuple(sorted([x, y, z])))

                    pass
                else:
                    pass

    print(len(result))

    pass


if __name__ == "__main__":
    main()
