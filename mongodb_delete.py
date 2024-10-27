from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

cluster=MongoClient(os.getenv("MONGO_CLUSTER_URI"))
db=cluster["jjinchin"]
collection = db["chats"]
collection.delete_many({})

# 아래는 메모리 db 삭제
# db=cluster["jjinchin"]
# collection = db["memory"]
# collection.delete_many({})