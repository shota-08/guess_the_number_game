import random

def get_input(prompt):
    """数値の入力を受け取り、整数にして返す。"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("数値を入力してください。")

def main():
    min_val = get_input("最小値を入力してください: ")
    max_val = get_input("最大値を入力してください: ")

    if min_val > max_val:
        print("error: 最大値は最小値以上の数値にしてください。")
        return main()

    answer = random.randint(min_val, max_val)
    attempts = 1

    while attempts <= 5:
        guess = get_input(f"{attempts}回目の挑戦: ")
        if guess == answer:
            return print("クリア!")
        else:
            print("残念!")
            attempts += 1

    print(f"正解は{answer}でした。また挑戦してね!")

if __name__ == "__main__":
    print("""ゲームをしましょう!\nまず、あなたが数字を二つ、最小値と最大値を入力します。その範囲内で、システムがランダムに数字を決めます。\n5回以内にその数字を当ててください!\n""")
    main()