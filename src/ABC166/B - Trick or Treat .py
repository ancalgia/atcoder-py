import itertools


def main(case: str) -> None:
    NK, *rest = [list(map(int, x.split())) for x in case.splitlines()]

    N, K = NK

    okasi_holders = [x for idx, x in enumerate(rest) if idx % 2 == 1]

    flat_okasi_holders = set(itertools.chain.from_iterable(okasi_holders))

    counter = 0

    # for x in range(N):
    #     if x + 1 in flat_okasi_holders:
    #         continue
    #     counter += 1

    print(N - len(flat_okasi_holders))


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
3 2
2
1 3
1
3
        """,
        """
3 3
1
3
1
3
1
3
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
