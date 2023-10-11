import itertools


def main(case: str) -> None:
    N, *Ws = case.splitlines()

    WsSet = set(Ws)

    if len(WsSet) != int(N):
        print("No")
        return

    expected_char = Ws[0][0]

    for x in Ws:
        if x[0] != expected_char:
            print("No")
            return

        expected_char = x[-1]

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
4
hoge
english
hoge
enigma
        """,
        """
9
basic
c
cpp
php
python
nadesico
ocaml
lua
assembly
        """,
        """
8
a
aa
aaa
aaaa
aaaaa
aaaaaa
aaa
aaaaaaa
        """,
        """
3
abc
arc
agc
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
