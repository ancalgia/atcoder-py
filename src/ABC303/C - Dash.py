import collections
import itertools


def main(case: str) -> None:
    (NMHK), S, *XYs = case.splitlines()

    N, M, HpStart, Kaifuku = list(map(int, NMHK.split()))

    itemsXYStrSet = {*XYs}

    currPositionXY = [0, 0]
    currHp = HpStart

    for s in S:
        currHp -= 1

        if currHp < 0:
            print("No")
            return

        if s == "R":
            currPositionXY[0] += 1
        elif s == "L":
            currPositionXY[0] -= 1
        elif s == "U":
            currPositionXY[1] += 1
        else:
            currPositionXY[1] -= 1

        strCurrPositionXY = str(currPositionXY[0]) + " " + str(currPositionXY[1])

        if strCurrPositionXY in itemsXYStrSet:
            pass
            if currHp < Kaifuku:
                currHp = Kaifuku
                itemsXYStrSet.remove(strCurrPositionXY)

    print("Yes")


if __file__.endswith("Main.py"):
    import sys

    case: str = "".join([x for x in sys.stdin])
    main(case)
    exit()


else:
    print("テスト")
    from textwrap import dedent

    test_list: list[str] = [
        """
4 2 3 1
RUDL
-1 -1
1 0
        """,
        """
5 2 1 5
LDRLD
0 0
-1 -1
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("##########テスト入力##########")
        print(test)
        print("   vvvvvvvv出力結果vvvvvvvv")
        main(test)
