def main(case: str) -> None:
    N, Xs = case.splitlines()

    N = int(N)

    Xs = list(map(int, Xs.split()))

    minX = min(Xs)
    maxX = max(Xs)

    curr_score = 0

    for pos in range(minX, maxX):
        pass
        tmp = sum([pow(x - pos, 2) for x in Xs])

        if tmp < curr_score or curr_score == 0:
            curr_score = tmp

    print(curr_score)


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
1 4
        """,
        """
7
14 14 2 13 56 2 37
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
