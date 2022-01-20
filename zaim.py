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


def outputJSON(datas, categories, genres, accounts):
    """取得したデータをJSON形式で出力する

    """

    new_path = "json"
    if not os.path.exists(new_path):
        os.mkdir(new_path)

    with open('json/zaim-backup.json', 'w') as f:
        json.dump(datas, f, ensure_ascii=False, indent=4)

    with open('json/category.json', 'w') as f:
        json.dump(categories, f, ensure_ascii=False, indent=4)

    with open('json/genre.json', 'w') as f:
        json.dump(genres, f, ensure_ascii=False, indent=4)

    with open('json/account.json', 'w') as f:
        json.dump(accounts, f, ensure_ascii=False, indent=4)
