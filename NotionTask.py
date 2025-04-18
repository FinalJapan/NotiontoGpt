from notion_client import Client
from dotenv import load_dotenv
import os

load_dotenv()

notion = Client(auth=os.getenv("NOTION_TOKEN"))
database_id = os.getenv("NOTION_DATABASE_ID")

try:
    response = notion.databases.query(database_id=database_id, page_size=1)
    print("✅ データ取得成功！")
    print(response)
except Exception as e:
    import traceback
    print("❌ エラー内容：")
    traceback.print_exc()
