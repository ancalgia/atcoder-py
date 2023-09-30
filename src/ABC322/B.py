def main(case: str) -> None:
    _, S, T = case.splitlines()

    result = 0
    isSetto = T.startswith(S)

    isSetsu = T.endswith(S)

    # S が T の接頭辞であり、かつ接尾辞でもある場合は
    # 0 を、
    # S が T の接頭辞であるが、接尾辞でない場合は
    # 1 を、
    # S が T の接尾辞であるが、接頭辞でない場合は
    # 2 を、
    # S が T の接頭辞でも接尾辞でもない場合は
    # 3 を出力してください。

    if isSetto:
        if isSetsu:
            print(0)
        else:
            print(1)

    else:
        if isSetsu:
            print(2)
        else:
            print(3)


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
        3 7
        abc
        abcdefg
        """,
        """
        3 4
        abc
        aabc
        """,
        """
        3 3
        abc
        xyz
        """,
        """
        3 3
        aaa
        aaa
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
