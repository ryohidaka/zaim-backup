# .env ファイルをロードして環境変数へ反映
import os
from dotenv import load_dotenv
load_dotenv()

# 環境変数を参照
CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_SECRET = os.environ.get('ACCESS_SECRET')
