from notion_client import Client
from dotenv import load_dotenv
import os

load_dotenv()

notion = Client(auth=os.getenv("NOTION_TOKEN"))
database_id = os.getenv("NOTION_DATABASE_ID")

# 試しに1件だけ取得してみよう
response = notion.databases.query(
    database_id=database_id,
    page_size=1
)

print("✅ 取得成功！", response["results"][0]["id"])
