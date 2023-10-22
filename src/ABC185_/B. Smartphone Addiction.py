import itertools


def main(case: str) -> None:
    (N, M, T), *rest = [list(map(int, x.split())) for x in case.splitlines()]

    currBattery = N

    currTime = 0

    for cafe in rest:
        elapsed = cafe[0] - currTime

        currBattery -= elapsed

        if currBattery <= 0:
            print("No")
            return

        cafeElapsed = cafe[1] - cafe[0]

        currBattery = min([currBattery + cafeElapsed, N])

        currTime = cafe[1]

    final = T - currTime

    if currBattery <= final:
        print("No")
    else:
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
10 2 20
9 11
13 17
        """,
        """
10 2 20
9 11
13 16
        """,
        """
15 3 30
5 8
15 17
24 27
        """,
        """
20 1 30
20 29
        """,
        """
20 1 30
1 10
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
