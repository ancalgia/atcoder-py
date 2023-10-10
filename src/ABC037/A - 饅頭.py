import itertools


def main(case: str) -> None:
    ABC, *S = case.splitlines()

    A, B, C = list(map(int, ABC.split()))

    to_buy = A if A <= B else B

    cnt = C // to_buy

    print(cnt)


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
3 5 6
        """,
        """
8 6 20
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
