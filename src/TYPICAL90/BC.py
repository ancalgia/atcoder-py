import itertools


def main(case: str) -> None:
    NPQ, A = case.splitlines()

    N, P, Q = map(int, NPQ.split())

    As = map(int, A.split())

    selections = itertools.combinations(As, 5)

    count = 0

    for x in selections:
        # prod = math.prod(x)
        # amari = ((x[0] % P) * (x[1] % P) * (x[2] % P) * (x[3] % P) * (x[4] % P)) % P
        amari = x[0] % P * x[1] % P * x[2] % P * x[3] % P * x[4] % P

        if amari == Q:
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
6 7 1
1 2 3 4 5 6
        """,
        """
10 1 0
0 0 0 0 0 0 0 0 0 0
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
