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
# 10
# 1 19 75 37 17 16 33 18 22
# 41 28 89 74 98 43 42 31
#     """
# ).strip()

# expected:
# 7
# 1_2_4_5_6_8_10


def main():
    # (N,), As, Bs = IALL(case)

    # roomTimes: list[tuple[int, list[int]]] = [(-1, []) for x in range(N)]

    # roomTimes[0] = (0, [1])

    # estList: list[tuple[int, list[int]]] = []

    # for x in range(N):
    #     estList.clear()

    #     if x == 0:
    #         continue

    #     if x >= 1:
    #         estList.append((roomTimes[x - 1][0] + As[x - 1], roomTimes[x - 1][1] + [x + 1]))

    #     if x >= 2:
    #         estList.append((roomTimes[x - 2][0] + Bs[x - 2], roomTimes[x - 2][1] + [x + 1]))

    #     roomTimes[x] = min(estList)

    # # print(roomTimes[-1])

    # print(len(roomTimes[-1][1]))

    # print(*roomTimes[-1][1])

    (N,), As, Bs = IALL(case)

    roomTimes: list[int] = [-1 for x in range(N)]

    roomTimes[0] = 0

    estList: list[int] = []

    for x in range(N):
        estList.clear()

        if x == 0:
            continue

        if x >= 1:
            estList.append(roomTimes[x - 1] + As[x - 1])

        if x >= 2:
            estList.append(roomTimes[x - 2] + Bs[x - 2])

        roomTimes[x] = min(estList)

    ans = [N]

    currRoom = N

    while True:
        if currRoom == 1:
            break

        if currRoom == 2:
            ans.append(1)
            break

        if roomTimes[currRoom - 1] == roomTimes[currRoom - 2] + As[currRoom - 2]:
            ans.append(currRoom - 1)
            currRoom -= 1
        else:
            ans.append(currRoom - 2)
            currRoom -= 2

    # for x in range(1, N):
    #     if x == N - 2:
    #         ans.append(1)
    #         break

    #     if roomTimes[-x] == roomTimes[-x - 1] + As[-x]:
    #         ans.append(ans[-1] - 1)
    #     else:
    #         ans.append(ans[-1] - 2)

    print(len(ans))

    print(*ans[::-1])


if __name__ == "__main__":
    main()
