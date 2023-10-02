def main(case: str) -> None:
    N, score = case.splitlines()

    scores = list(map(int, score.split()))

    scores.sort()

    filtered = scores[int(N) : -int(N)]

    print(sum(filtered) / (3 * int(N)))


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
        1
        10 100 20 50 30
        """,
        """
        2
        4 3 3 3 5 6 7 8 99 100
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
