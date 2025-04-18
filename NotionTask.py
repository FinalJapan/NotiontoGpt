from notion_client import Client
from dotenv import load_dotenv
import os

# .envからトークンを読み込む
load_dotenv()
notion_token = os.getenv("NOTION_TOKEN")
database_id = os.getenv("NOTION_DATABASE_ID")  # データベースIDも.envで管理すると安全！

# Notionクライアント初期化
notion = Client(auth=notion_token)

# データベースからデータ取得
response = notion.databases.query(database_id=database_id)

print("✅ タスク一覧（タイトルだけ表示）")
for result in response["results"]:
    props = result["properties"]
    
    # タイトルプロパティ名（例："タスク名" など）を合わせてね！
    try:
        title = props["タスク名"]["title"][0]["plain_text"]
        print("-", title)
    except Exception:
        print("⚠️ タイトルなし or フォーマット違いの項目あり")
