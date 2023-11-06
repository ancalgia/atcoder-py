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
    X, Y, Z = IL(case)

    # 考えるのが面倒なので正の方向にゴールがあることにする
    if X < 0:
        X = -X
        Y = -Y
        Z = -Z

    if 0 <= Y <= X:
        # 間に壁あり

        if Y < Z:
            # ハンマーが取れない
            print(-1)
            return

        elif Z < 0:
            # ハンマーを取りに後進
            print(abs(Z) * 2 + X)

        else:
            # 歩くだけでクリア
            print(X)

    elif Y < 0 or X < Y:
        # 間に壁なし
        print(X)


if __name__ == "__main__":
    main()
