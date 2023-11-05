def main(case: str) -> None:
    x, *y = case.splitlines()

    for idx, hoge in enumerate(y):
        if idx % 2 == 1:
            num_list = list(map(int, hoge.split()))

            print(len([x for x in num_list if x % 2 == 1]))


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
        4
        3
        1 2 3
        2
        20 23
        10
        6 10 4 1 5 9 8 6 5 1
        1
        1000000000
        """,
        # """
        # 4
        # 2023
        # Year
        # New
        # Happy
        # """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
