import itertools


def main(case: str) -> None:
    N, *As = case.splitlines()

    N = int(N)

    setAs = set(As)

    dictAs: dict[str, int] = dict([(x, 0) for x in setAs])

    results = As.copy()

    for idx, a in enumerate(As):
        count = dictAs.get(a)
        if count != 0:
            results[idx] = results[idx] + "(" + str(count) + ")"

        dictAs[a] += 1

    print("\n".join(results))


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
newfile
newfile
newfolder
newfile
newfolder
        """,
        """
11
a
a
a
a
a
a
a
a
a
a
a
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
