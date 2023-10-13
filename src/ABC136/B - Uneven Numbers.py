import itertools


def main(case: str) -> None:
    N, *_ = case.splitlines()

    count = 0

    ketasu = len(N)

    if ketasu == 1:
        print(N)
        return

    for x in range(1, ketasu):
        if x % 2 == 0:
            continue

        count += int("9" + ("0" * (x - 1)))

    if ketasu % 2 == 1:
        count += int(N) - int("9" * (ketasu - 1))

    print(f"{count}")


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
0
        """,
        """
200
        """,
        """
100001
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
