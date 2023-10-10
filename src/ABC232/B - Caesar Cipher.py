import itertools


def main(case: str) -> None:
    S, T = case.splitlines()

    if S == T:
        print("Yes")
        return

    caesar = str.maketrans("abcdefghijklmnopqrstuvwxyz", "zabcdefghijklmnopqrstuvwxy")

    for x in range(26):
        S = S.translate(caesar)

        if S == T:
            print("Yes")
            return

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
abc
ijk
        """,
        """
z
a
        """,
        """
ppq
qqp
        """,
        """
atcoder
atcoder
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
