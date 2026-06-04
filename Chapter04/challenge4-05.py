def convert(string):
    try:
        return float(string)
    except ValueError:
        print("数字か少数点数を入力してください")

c = convert("ああああ")
print(c)

