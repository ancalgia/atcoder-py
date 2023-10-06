def main(case: str) -> None:
    NK, *ab = case.splitlines()

    N, K = map(int, NK.split())

    large_list = sorted([sorted(map(int, x.split()), reverse=True)[0] for x in ab])

    count = 0

    current = -1

    already_exists = True

    for num in large_list:
        if current == num:
            # 同じ数字
            already_exists = True

        else:
            # 数字変わった
            current = num
            if not already_exists:
                count += 1

            already_exists = False
            continue

    if not already_exists:
        count += 1

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
5 5
1 2
1 3
3 2
5 2
4 2
        """,
        """
2 1
1 2
        """,
        """
7 18
7 2
1 6
5 2
1 3
7 6
5 3
5 6
5 4
1 7
2 6
3 4
5 1
4 7
4 6
5 7
3 2
4 2
1 4
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
