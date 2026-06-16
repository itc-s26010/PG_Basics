#文字列の中で該当する特定の文字を全て置き換える
equ = "All animals sre equal."
equ = equ.replace("a","@")
print(equ)

#特定文字が1文字だけなら1文字だけ置き換えることも可能
author = "Kafka"
author = author.replace("f","v")
print(author)

