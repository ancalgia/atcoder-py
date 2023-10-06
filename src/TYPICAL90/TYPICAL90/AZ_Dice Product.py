import bisect
import itertools
import math

magic_num = 10**9 + 7


def magic_prod(l) -> int:
    current = 1

    for x in l:
        current = current * x

        if current > magic_num:
            current = current % magic_num

    return current


def main(case: str) -> None:
    N, *As = [list(map(int, x.split())) for x in case.splitlines()]

    calced_As = [sum(x) for x in As]

    all_scores = magic_prod(calced_As)

    print(all_scores)


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
2
1 2 3 5 7 11
4 6 8 9 10 12
        """,
        """
1
11 13 17 19 23 29
            """,
        """
7
19 23 51 59 91 99
15 45 56 65 69 94
7 11 16 34 59 95
27 30 40 43 83 85
19 23 25 27 45 99
27 48 52 53 60 81
21 36 49 72 82 84
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
