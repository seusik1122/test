from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

app = FastAPI()

# Firebase 연결
cred = credentials.Certificate("firebase-key.json")
firebase_admin.initialize_app(cred)

# DB 객체 생성
db = firestore.client()


# 데이터 저장
@app.post("/save")
def save_item():

    data = {
        "item_name": "에어팟",
        "category": "고가품",
        "freshness": "N/A",
        "status": "보관중"
    }

    db.collection("lost_items").add(data)

    return {"message":"저장 완료"}


# 데이터 조회
@app.get("/items")
def get_items():

    docs = db.collection("lost_items").stream()

    result = []

    for doc in docs:
        item = doc.to_dict()
        item["id"] = doc.id
        result.append(item)

    return result