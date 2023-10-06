import math


def main(case: str) -> None:
    A, B, C = map(int, case.split())

    koyaku = math.gcd(A, B, C)

    ans = (A // koyaku) + (B // koyaku) + (C // koyaku) - 3

    print(ans)


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
        2 2 3
        """,
        """
        2 2 4
        """,
        """
        1000000000000000000 999999999999999999 999999999999999998
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
