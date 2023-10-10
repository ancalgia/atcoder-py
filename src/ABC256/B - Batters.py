import itertools


def main(case: str) -> None:
    (N,), As = [list(map(int, x.split())) for x in case.splitlines()]

    curr_runners = []

    for x in range(N):
        move = As[x]

        if move == 1:
            curr_runners = [1] + curr_runners
        elif move == 2:
            curr_runners = [0, 1] + curr_runners
        elif move == 3:
            curr_runners = [0, 0, 1] + curr_runners
        else:
            curr_runners = [0, 0, 0, 1] + curr_runners

    score = sum([x for x in curr_runners[3:]])

    print(score)


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
        1 1 3 2
                """,
        """
        3
        1 1 1
                """,
        """
10
2 2 4 1 1 1 4 2 2 1
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
