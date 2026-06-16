#formatによる書式指定を変数に入れてから表示
What = input("何が:")
When = input("いつ:")
Where = input("どこで:")
do = input("どうした:")

r = "{}は{}、{}で{}。".format(What, When, Where, do)
print(r)
#f文字列を使っての書式指定だとこうなります
print(f"{What}は{When}、{Where}で{do}。")
