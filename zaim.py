import config
from pyzaim import ZaimAPI
import os
import json
import csv


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


def outputCSV(datas):
    """カラム名を日本語に置換し、CSV出力する

    """

    # 種別名を日本語に置換
    for data in datas:
        keys = {
            "date": "日付",
            "mode": "方法",
            "category": "カテゴリ",
            "genre": "カテゴリの内訳",
            "from": "支払元",
            "to": "入金先",
            "name": "品目",
            "comment": "メモ",
            "place": "お店",
            "currency_code": "通貨"
        }
        for k, v in keys.items():
            data[v] = data.pop(k)

        # 入出金
        data["収入"] = data.pop("amount") if data["方法"] == "income" else 0
        data["支出"] = data.pop("amount") if data["方法"] == "payment" else 0
        data["振替"] = data.pop("amount") if data["方法"] == "transfer" else 0

        # 不要なキーを削除
        unUsedKeys = ["id", "user_id", "category_id",
                      "genre_id", "from_account_id", "to_account_id", "active", "created", "receipt_id", "place_uid", "original_money_ids"]
        for key in unUsedKeys:
            if(key in data):
                data.pop(key)

    # ヘッダーを指定
    fieldName = list(keys.values())
    fieldName.extend(['収入', '支出', '振替'])

    # CSV出力
    with open('zaim-backup.csv', 'w', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldName)
        writer.writeheader()
        writer.writerows(datas)


def outputJSON(datas):
    """取得したデータをJSON形式で出力する

    """

    with open('zaim-backup.json', 'w') as f:
        json.dump(datas, f, ensure_ascii=False, indent=4)
