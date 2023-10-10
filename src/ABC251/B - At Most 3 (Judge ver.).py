import itertools


def main(case: str) -> None:
    NW, As = case.splitlines()

    N, W = list(map(int, NW.split()))

    As = list(map(int, As.split()))

    good_numbers: list[int] = []

    select1 = list(itertools.combinations(As, 1))

    good_numbers.extend([sum(x) for x in select1 if sum(x) <= W])

    if N < 2:
        print(len(set(good_numbers)))
        return

    select2 = list(itertools.combinations(As, 2))

    good_numbers.extend([sum(x) for x in select2 if sum(x) <= W])

    if N < 3:
        print(len(set(good_numbers)))
        return

    select3 = list(itertools.combinations(As, 3))

    good_numbers.extend([sum(x) for x in select3 if sum(x) <= W])

    print(len(set(good_numbers)))


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
2 10
1 3
        """,
        """
2 1
2 3
        """,
        """
4 12
3 3 3 3
        """,
        """
7 251
202 20 5 1 4 2 100
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
