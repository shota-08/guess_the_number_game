# 🎯 数当てゲーム (Number Guessing Game)

## 📖 概要
- プレイヤーが指定した範囲内でランダムに選ばれた数字を5回以内に当てるシンプルなコンソールゲームです。

## 🎮 遊び方
1. 最小値と最大値を入力する
    - 例: 「10」と「50」を入力すると、その範囲の中からランダムに数が選ばれます
    - 最小値 > 最大値の場合はエラーが出て再入力になります
2. システムがランダムな数を選ぶ
    - 例えば、システムが「25」を選んだとします
3. 5回以内に正解を当てる
    - 数値を入力し、正解なら「クリア!」と表示
    - 間違えたら「残念!」と表示され、次の挑戦へ
4. 5回失敗した場合、答えが表示される
    - 「正解は 25 でした。また挑戦してね!」のように答えが出ます。

## 🚀 実行方法
以下のスクリプトを実行
```
python main.py
```