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
    (N, D), *XYs = IALL(case)

    persons = []

    for x, y in XYs:
        persons.append([x, y, False, False])

    persons[0][2] = True

    virused = 0

    while True:
        tmp = [x for x in persons if x[2]]

        if tmp == virused:
            break

        virused = tmp

        for x in range(N):
            if not persons[x][2] or persons[x][3]:
                continue

            persons[x][3] = True

            x1 = persons[x][0]
            y1 = persons[x][1]

            for y in range(N):
                if persons[y][2]:
                    continue

                dist = math.sqrt((persons[y][0] - x1) ** 2 + (persons[y][1] - y1) ** 2)

                if dist <= D:
                    persons[y][2] = True

    for x in persons:
        print("Yes") if x[2] else print("No")

    pass


if __name__ == "__main__":
    main()
