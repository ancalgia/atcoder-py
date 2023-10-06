import bisect
import itertools
import math

# TLEになるなら尺取りやるか？


def main(case: str) -> None:
    L, R = case.splitlines()

    if len(R) == 1:
        print(0)
        return

    counter = 0

    start = 0
    end = 1

    tgtstr = "x" if R[start] == "o" else "o"

    while True:
        if start == len(R) or end == len(R):
            print(counter)
            return

        if R[end] == tgtstr:
            counter += len(R) - end
            start += 1
            tgtstr = "x" if R[start] == "o" else "o"

        else:
            end += 1


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
4
ooxo
        """,
        """
5
oxoxo
        """,
        """
5
ooooo
        """,
        """
7
xxoooxx
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
