import itertools
import math
from typing import Literal


def main(case: str) -> None:
    NM, Ss, Ts = case.splitlines()

    N, M = list(map(int, NM.split()))

    TsSet = set(Ts.split())

    for x in Ss.split():
        if x in TsSet:
            print("Yes")
        else:
            print("No")


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
5 3
tokyo kanda akiba okachi ueno
tokyo akiba ueno
        """,
        """
7 7
a t c o d e r
a t c o d e r
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
