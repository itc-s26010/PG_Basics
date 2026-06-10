#リストを入れるリストを作る
lists = []
#listsの中に入れるリストを用意する
rap = ["カニエ・ウェスト","ジェイ・ｚ","エミネム","ナズ"]
rock = ["ボブ・ディラン","ザ・ビートルズ","レッド・ツェッペリン"]
djs = ["ゼッズ・デッド","ティエスト"]
#listsの中に各リストをappendしていく
lists.append(rap)
lists.append(rock)
lists.append(djs)
print(lists)

rap = lists[0]
print(rap)
rap.append("ケンドリック・ラマー")
print(rap)
print(lists)
