def main(case: str) -> None:
    NK, A, B = case.splitlines()

    N, K = map(int, NK.split())

    As = list(map(int, A.split()))
    Bs = list(map(int, B.split()))

    diffs = 0

    for x in range(N):
        diffs += abs(As[x] - Bs[x])

    if K < diffs:
        print("No")
        return

    if K % 2 != diffs % 2:
        print("No")
        return

    print("Yes")


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
2 5
1 3
2 1
        """,
        """
3 1
7 8 9
7 8 9
        """,
        """
7 999999999
3 1 4 1 5 9 2
1 2 3 4 5 6 7
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
