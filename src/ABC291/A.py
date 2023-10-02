def main(case: str) -> None:
    # x, *y = case.splitlines()
    # pass

    count = 0
    for c in case:
        count += 1
        if c.isupper():
            print(count)


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
        aBc
        """,
        """
        xxxxxxXxxx
        """,
        """
        Zz
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
