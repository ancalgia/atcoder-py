import bisect
import itertools
import math


def main(case: str) -> None:
    T, LXY, Q, *Es = case.splitlines()

    L_height, X, Y = map(int, LXY.split())

    questions = map(int, Es)

    chokudai_position = (X, Y, 0)

    def get_position(min: int) -> tuple[float, float, float]:
        hoge = math.modf(min / int(T))[0]

        if hoge > 0.5:
            pass
            position = (0, L_height * (hoge - 0.5) * 2, L_height * (hoge - 0.5) * 2)
        elif hoge == 0.5:
            position = (0, 0, L_height)
        else:
            position = (0, -L_height * hoge * 2, L_height * hoge * 2)
            pass

        return position

    def print_kakudo(me: tuple[float, float, float]):
        # distance = math.sqrt(abs(chokudai_position[0] - me[0]) ** 2 + abs(chokudai_position[1] - me[1]) ** 2)
        distance = math.sqrt(abs(chokudai_position[0]) ** 2 + abs(chokudai_position[1] - me[1]) ** 2)

        print(math.degrees(math.atan2(me[2], distance)))
        print(math.degrees(math.atan2(distance, me[2])))

    for x in questions:
        position = get_position(x)

        print_kakudo(position)


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
2 1 1
4
0
1
2
3
        """,
        """
5121
312000000 4123 3314
6
123
12
445
4114
42
1233
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
