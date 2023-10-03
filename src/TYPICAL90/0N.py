def main(case: str) -> None:
    N, As, Bs = case.splitlines()

    children = sorted(map(int, As.split()))

    schools = sorted(map(int, Bs.split()))

    ans = sum([abs(x[0] - x[1]) for x in zip(schools, children)])

    print(ans)


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
869
120
        """,
        """
6
8 6 9 1 2 0
1 5 7 2 3 9
        """,
        """
10
31 41 59 26 53 58 97 93 23 84
17 32 5 8 7 56 88 77 29 35
        """,
        """
20
804289382 846930886 681692776 714636914 957747792 424238335 719885386 649760491 596516649 189641420 25202361 350490026 783368690 102520058 44897761 967513925 365180539 540383425 304089172 303455735
35005211 521595368 294702567 726956428 336465782 861021530 278722862 233665123 145174065 468703135 101513928 801979801 315634021 635723058 369133068 125898166 59961392 89018454 628175011 656478041
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
