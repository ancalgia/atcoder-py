import itertools

import numpy


def main(case: str) -> None:
    HW, *rest = case.splitlines()

    H, W = list(map(int, HW.split()))

    rows = [x for x in rest]

    for x in range(len(rows)):
        rows[x] = rows[x].replace("TT", "PC")
        print(rows[x])


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
2 3
TTT
T.T
        """,
        """
3 5
TTT..
.TTT.
TTTTT
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
