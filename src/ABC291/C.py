def main(case: str) -> None:
    N, S = case.splitlines()

    trace_list: set[tuple[int, int]] = {(0, 0)}
    currX = 0
    currY = 0
    # S の i 文字目が R であるとき
    # (x+1,y)
    # S の i 文字目が L であるとき
    # (x−1,y)
    # S の i 文字目が U であるとき
    # (x,y+1)
    # S の i 文字目が D であるとき
    # (x,y−1)

    for move in S:
        if move == "R":
            currX += 1
        if move == "L":
            currX -= 1
        if move == "U":
            currY += 1
        if move == "D":
            currY -= 1

        tpl = (currX, currY)

        if tpl in trace_list:
            print("Yes")
            return

        trace_list.add((currX, currY))

    print("No")


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
        5
        RLURU
        """,
        """
        20
        URDDLLUUURRRDDDDLLLL
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
