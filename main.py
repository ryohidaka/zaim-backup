import zaim

# データ取得
datas, categories, genres, accounts = zaim.getZaimData()

# JSON出力
zaim.outputJSON(datas, categories, genres, accounts)
