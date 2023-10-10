import itertools
import math

# NOTE:三角関数わからんのでまだ
# NOTE:三角関数わからんのでまだ
# NOTE:三角関数わからんのでまだ
# NOTE:三角関数わからんのでまだ
# NOTE:三角関数わからんのでまだ


def main(case: str) -> None:
    A, B, D = list(map(int, case.split()))

    rad = math.radians(D)

    good_numbers: list[int] = []


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
2 2 180
        """,
        """
5 0 120
        """,
        """
0 0 11
        """,
        """
15 5 360
        """,
        """
-505 191 278
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
