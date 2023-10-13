import itertools


def main(case: str) -> None:
    (N,), *rest = [list(map(int, x.split())) for x in case.splitlines()]

    beautifulNumbers: list[int] = []

    for x in range(100000, 1000000):
        beautifulNumbers.append(x)

    tgt = list(str(beautifulNumbers[N - 1]))

    print(tgt[0] + tgt[0] + tgt[1] + tgt[2] + tgt[3] + tgt[3] + tgt[4] + tgt[5] + tgt[4])


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
3
        """,
        """
882436
        """,
        """
2023
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
