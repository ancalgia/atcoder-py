import itertools


def main(case: str) -> None:
    (N, X), As = [list(map(int, x.split())) for x in case.splitlines()]

    secret_friends = set()

    next_friend = X

    while True:
        if next_friend in secret_friends:
            print(len(secret_friends))
            return

        secret_friends.add(next_friend)

        next_friend = As[next_friend - 1]


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
4 2
3 1 1 2
        """,
        """
20 12
7 11 10 1 7 20 14 2 17 3 2 5 19 20 8 14 18 2 10 10
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
