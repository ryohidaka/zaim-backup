import zaim

# データ取得
datas, categories, genres, accounts = zaim.getZaimData()

# 種別名を付与する
datas = zaim.convertData(datas, categories, genres, accounts)

# JSON出力
zaim.outputJSON(datas)
