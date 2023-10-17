TODO: make .md File

# 環境構築っぽい話

## 仮想環境作成

python -m venv venv

## 仮想環境起動

source ./venv/bin/activate

↑LINUX
↓WIN

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process; ./venv/Scripts/Activate.ps1
or
./venv/Scripts/Activate.ps1

ライブラリのインストール
pip install -r requirements.txt

## online-judge-tools atcoder-cli とかのメモ

atcoder-cli、online-judge-tools を java で環境構築する - Qiita
https://qiita.com/hario/items/20b78cf56634289f79c1

Windows 10 上で atcoder-cli を online-judge-tools と連携させて使う：導入からテストと提出までの基本的操作 - はむ吉（のんびり）の練習ノート
https://hamukichi.hatenablog.jp/entry/2020/06/02/225148

AtCoder 環境構築[online-judge-tools][atcoder-cli][Java]
https://zenn.dev/karaageeeee/articles/b3a49cc1c179a5

Matched languages were not narrowed down to one.

VSCode + Docker で AtCoder のテスト・提出ができる環境構築【Python,PyPy】 - Qiita
https://qiita.com/gomatofu/items/1adae9b7cd79b0f8044f

atcoder-cli のデフォルト提出言語を PyPy3 に設定する | foolish-pine.com
https://foolish-pine.com/posts/2022/09/acc-default-pypy

# コンテスト時の流れ

## src ディレクトリに移動

## コンテストフォルダ作成

### コンテスト作成するときのコマンド

```
acc new {abcなんとか} --template python
```

例:
acc new abc??? --template python

## 問題ディレクトリに移動

## main.py いじる

## テストケース検証

### テスト用コマンド

```
oj t -c "python main.py"
```

## SUBMIT

### SUBMIT 用コマンド

```
acc s main.py -- --guess-python-interpreter pypy
```

#### コマンドだけまとめ

1. コンテスト作成

acc new abc??? --template python

編集用
acc new abc044 --template python

2. テスト

oj t -c "python main.py"

3. 提出

acc s main.py -- --guess-python-interpreter pypy
