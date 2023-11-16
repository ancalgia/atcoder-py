#!/usr/bin/env python3

import bisect, collections, copy, heapq, itertools, math, string  # isort: skip
import sys


# fmt: off
def SL(s: str) -> list[str]: return s.splitlines()
def IL(s: str) -> list[int]: return list(map(int, s.split()))
def IALL(s: str) -> list[list[int]]: return [list(map(int, x.split())) for x in s.splitlines()]
# fmt: on


case: str = "".join([x for x in sys.stdin])


# NOTE：これ全部間違ってるんで素直にDPの勉強しよう


def main():
    (N,), *XYs = IALL(case)

    fileteredXYs = [(x[0], x[1]) for x in XYs if (x[0] == 0 or x[1] > 0)]

    score = 0

    suspendedPoison: int = 0

    suspendedMedicine: list[int] = []

    for x, y in fileteredXYs:
        if x == 0:
            # 解毒剤入り
            if y >= 0:
                # おいしいので当然食べる
                score += y
                # 保留中の毒入りがあれば一番おいしいやつを食べる
                score += suspendedPoison
                # 全てを忘れる
                suspendedPoison = 0
                suspendedMedicine.clear()

            else:
                # 薬だが、まずい
                if suspendedPoison == 0:
                    # 毒の保留がなければ食べる（保留する）価値なし
                    continue

                # 保留中の毒と合わせても食べる価値があるなら纏めて食べる
                if suspendedPoison + y > 0:
                    suspendedMedicine.append(y)
                    # score += suspendedPoison + y
                    # suspendedPoison = 0

        else:
            if len(suspendedMedicine) > 0:
                # 薬を持ってる時に毒をが出たので一旦整理
                if max(suspendedMedicine) + suspendedPoison > 0:
                    # 価値があるなら一番いいものを食べる
                    score += max(suspendedMedicine) + suspendedPoison

                    # 食べたら片づける
                    suspendedMedicine.clear()
                    suspendedPoison = 0

                else:
                    # 価値がなければ薬だけ片づける
                    suspendedMedicine.clear()

            # 毒料理の中で一番おいしいものをキープ
            suspendedPoison = max(suspendedPoison, y)

    print(score + suspendedPoison)


if __name__ == "__main__":
    main()
