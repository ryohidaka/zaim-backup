import config
from pyzaim import ZaimAPI
import os
import json


def getZaimData():
    """Zaimのデータを取得する

    """

    consumer_key = config.CONSUMER_KEY
    consumer_secret = config.CONSUMER_SECRET
    access_token = config.ACCESS_TOKEN
    access_secret = config.ACCESS_SECRET

    api = ZaimAPI(consumer_key, consumer_secret,
                  access_token, access_secret, 'verifier')
    # データ一覧の取得
    datas = api.get_data()

    # カテゴリ一覧情報
    categories = api.category_itos

    # ジャンル一覧情報を取得
    genres = api.genre_itos

    # 口座一覧情報を取得
    accounts = api.account_itos

    msg = str(len(datas)) + " 件のデータを取得しました"
    print(msg)

    return [datas, categories, genres, accounts]


def convertData(datas, categories, genres, accounts):
    """種別IDをもとに、種別名を付与する

    """

    for data in datas:

        # カテゴリ名を付与
        categoryId = int(data["category_id"])
        data["category"] = categories[categoryId] if categoryId > 0 else ""

        # 内訳名を付与
        genreId = int(data["genre_id"])
        data["genre"] = genres[genreId] if genreId > 0 else ""

        # 口座名を付与
        fromAccountId = int(data["from_account_id"])
        data["from"] = accounts[fromAccountId] if fromAccountId > 0 else "-"

        toAccountId = int(data["to_account_id"])
        data["to"] = accounts[toAccountId] if toAccountId > 0 else "-"

    return datas


def outputJSON(datas):
    """取得したデータをJSON形式で出力する

    """

    with open('zaim-backup.json', 'w') as f:
        json.dump(datas, f, ensure_ascii=False, indent=4)
