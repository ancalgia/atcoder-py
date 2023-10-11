import itertools
from typing import Literal


def main(case: str) -> None:
    S, T = case.splitlines()

    regular_charset = set(["a", "t", "c", "o", "d", "e", "r"])

    legal_win = True

    for x in range(len(S)):
        if (S[x] == "@" and T[x] in regular_charset) or (T[x] == "@" and S[x] in regular_charset) or S[x] == T[x]:
            continue
        else:
            legal_win = False

    if legal_win:
        print("Yes")
        return

    sorted_S_chars: list[str] = sorted([*S])
    sorted_T_chars: list[str] = sorted([*T])

    regular_charset = set(["a", "t", "c", "o", "d", "e", "r"])

    irregular_S_chars = [x for x in sorted_S_chars if x not in regular_charset and x != "@"]
    irregular_T_chars = [x for x in sorted_T_chars if x not in regular_charset and x != "@"]

    irregular_S_char_counts: dict[str, int] = dict()
    irregular_T_char_counts: dict[str, int] = dict()

    for charS in irregular_S_chars:
        if charS in irregular_S_char_counts.keys():
            irregular_S_char_counts[charS] += 1
        else:
            irregular_S_char_counts[charS] = 1

    for charT in irregular_T_chars:
        if charT in irregular_T_char_counts.keys():
            irregular_T_char_counts[charT] += 1
        else:
            irregular_T_char_counts[charT] = 1

    pass

    for charS in irregular_S_char_counts:
        if charS not in irregular_T_char_counts.keys():
            # 同じキーがもう片方にもなければエラー
            print("No")
            return

        if irregular_S_char_counts[charS] != irregular_T_char_counts[charS]:
            # 数が違ってもエラー
            print("No")
            return

    # 冗長ぽいが多分処理は軽いので反対からも確認
    for charT in irregular_T_char_counts:
        if charT not in irregular_S_char_counts.keys():
            # 同じキーがもう片方にもなければエラー
            print("No")
            return

        if irregular_T_char_counts[charT] != irregular_S_char_counts[charT]:
            # 数が違ってもエラー
            print("No")
            return

    atmark_count = len([x for x in sorted_S_chars + sorted_T_chars if x == "@"])

    regular_S_chars = [x for x in sorted_S_chars if x in regular_charset]
    regular_T_chars = [x for x in sorted_T_chars if x in regular_charset]

    regular_S_char_counts: dict[str, int] = dict()
    regular_T_char_counts: dict[str, int] = dict()

    for charS in regular_S_chars:
        if charS in regular_S_char_counts.keys():
            regular_S_char_counts[charS] += 1
        else:
            regular_S_char_counts[charS] = 1

    for charT in regular_T_chars:
        if charT in regular_T_char_counts.keys():
            regular_T_char_counts[charT] += 1
        else:
            regular_T_char_counts[charT] = 1

    must_change_count = 0

    for keys in ["a", "t", "c", "o", "d", "e", "r"]:
        countS = regular_S_char_counts.get(keys) or 0
        countT = regular_T_char_counts.get(keys) or 0

        must_change_count += abs(countS - countT)

    if atmark_count >= must_change_count:
        print("Yes")
    else:
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
ch@ku@ai
choku@@i
        """,
        """
ch@kud@i
akidu@ho
        """,
        """
aoki
@ok@
        """,
        """
aa
bb
        """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
