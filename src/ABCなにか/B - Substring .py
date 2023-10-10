# import bisect


def main(case: str) -> None:
    S,T = case.splitlines()

    max = len(T)

    try:    
        for x in range(len(S)):

            counter = len(T)        
            for y in range(len(T)):
                if S[x+y] == T[y]:
                    counter -=1 
            
            if counter <max:
                max = counter        
        
        print (max)

    except:
        print(max)
        
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
cabacc
abc
        """,
        """
codeforces
atcoder
        """,
#         """
# 10000 1 1
#         """,
    ]

    dd = dedent

    formatted_test_list = [dd(x).strip() for x in test_list]

    for test in formatted_test_list:
        print("*･゜･*:.｡..｡.:*･゜テスト入力･*:.｡. .｡.:*･゜･* ")
        print(test)
        print("↓↓↓出力結果↓↓↓")
        main(test)
