def main(case: str) -> None:
    NM, T = case.splitlines()

    # N日　M回
    N, M = map(int, NM.split())

    fire_days = list(map(int, T.split()))

    # days = [0] * N

    is_fire_list: list[int] = [0] * N

    for fire_day in fire_days:
        # is_fire_list[fire_day] = True
        # is_fire_list[fire_day - 1] = True
        is_fire_list[fire_day - 1] = 1

    # is_fire_list = [1 if (x[0] + 1) in fire_days else 0 for x in enumerate(days)]

    pass

    is_fire_list.reverse()

    output_list: list[int] = []

    curr: int = 0

    for x in is_fire_list:
        if x == 1:
            curr = 0
            output_list.append(curr)

        else:
            curr += 1
            output_list.append(curr)

    output_list.reverse()

    for x in output_list:
        print(x)

    # last_answer: int = 0

    # for out_idx in range(N):
    #     # from_today = is_fire_list[out_idx:]

    #     if last_answer > 0:
    #         last_answer -= 1
    #         print(last_answer)
    #         continue

    #     for idx, c in enumerate(is_fire_list[out_idx:]):
    #         # if c:
    #         if c:
    #             last_answer = idx
    #             print(idx)
    #             break


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
        2 3
        """,
        """
        8 5
        1 3 4 7 8
        """,
        # """
        # 3 3
        # abc
        # xyz
        # """,
        # """
        # 3 3
        # aaa
        # aaa
        # """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
