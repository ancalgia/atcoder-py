import itertools


def main(case: str) -> None:
    N, S = case.splitlines()

    caesar = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "BCDEFGHIJKLMNOPQRSTUVWXYZA")

    for x in range(int(N)):
        S = S.translate(caesar)

    print(S)


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
ABCXYZ
        """,
        """
0
ABCXYZ
        """,
        """
13
ABCDEFGHIJKLMNOPQRSTUVWXYZ
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
