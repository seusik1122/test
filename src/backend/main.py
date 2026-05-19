from fastapi import FastAPI
from pydantic import BaseModel
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime, timedelta

app = FastAPI()

# Firebase 연결
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase-key.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()


class BBox(BaseModel):
    x: int
    y: int
    w: int
    h: int


class LostItem(BaseModel):
    object_name: str
    category: str
    image_url: str
    full_image_url: str
    yolo_confidence: float
    freshness: str
    camera_id: str
    raw_ai_response: str
    bbox: BBox


@app.get("/")
def home():
    return {"message": "서버 실행 중"}


@app.post("/save")
def save_item(item: LostItem):

    dispose_days_map = {
        "음식물": 1,
        "비음식물": 30,
        "고가품": 180
    }

    dispose_days = dispose_days_map.get(
        item.category,
        30
    )

    data = {
        "object_name": item.object_name,
        "category": item.category,
        "dispose_days": dispose_days,
        "found_at": datetime.now(),
        "dispose_at": datetime.now() + timedelta(days=dispose_days),
        "status": "stored",
        "image_url": item.image_url,
        "full_image_url": item.full_image_url,
        "bbox": item.bbox.dict(),
        "yolo_confidence": item.yolo_confidence,
        "freshness": item.freshness,
        "camera_id": item.camera_id,
        "raw_ai_response": item.raw_ai_response,
        "notified": False
    }

    db.collection("lost_items").add(data)

    return {"message": "저장 완료"}


@app.get("/items")
def get_items():

    docs = db.collection("lost_items").stream()

    result = []

    for doc in docs:
        item = doc.to_dict()
        item["id"] = doc.id
        result.append(item)

    return result