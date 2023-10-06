import bisect
import itertools
import math


def main(case: str) -> None:
    A, B, C = map(int, case.split())

    # print("Yes" if math.log2(A) < math.log2(C) * B else "No")
    print("Yes" if A < C**B else "No")


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
4 3 2
        """,
        """
16 3 2
        """,
        """
8 3 2
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
