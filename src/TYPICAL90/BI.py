def main(case: str) -> None:
    Q, *txs = case.splitlines()

    cards: list[int] = []

    for tx in txs:
        t, x = map(int, tx.split())

        if t == 1:
            cards.append(x)
        elif t == 2:
            cards.insert(0, x)
        elif t == 3:
            print(cards[-x])


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
6
1 2
1 1
2 3
3 1
3 2
3 3
        """,
        """
6
2 1
3 1
2 2
3 1
2 3
3 1
        """,
        """
6
1 1000000000
2 200000000
1 30000000
2 4000000
1 500000
3 3
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
