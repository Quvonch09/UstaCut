from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from bot import send_to_admin  # ✅ oldin: from app.bot import send_to_admin

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # keyin hosting domenini ham qo‘shamiz
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Booking(BaseModel):
    barber: str
    client_name: str
    phone: str
    date: str
    time: str
    service: str
    comment: str | None = None

BOOKED: set[str] = set()

@app.post("/book")
async def book(data: Booking):
    key = f"{data.barber}_{data.date}_{data.time}"
    if key in BOOKED:
        return {"ok": False, "message": "Bu vaqt band"}

    BOOKED.add(key)
    await send_to_admin(data)
    return {"ok": True}

@app.get("/available-times")
async def available_times(barber: str, date: str):
    all_times = ["9:00","10:00","11:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00"]
    booked_times = [
        key.split("_")[2]
        for key in BOOKED
        if key.startswith(f"{barber}_{date}")
    ]
    return [t for t in all_times if t not in booked_times]
