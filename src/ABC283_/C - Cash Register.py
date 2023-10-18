import itertools


def main(case: str) -> None:
    S, *_ = case.splitlines()

    deleted00 = S.replace("00", "")

    deleted_count = (len(S) - len(deleted00)) // 2

    print(len(deleted00) + deleted_count)


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
40004
        """,
        """
1355506027
        """,
        """
10888869450418352160768000001
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
