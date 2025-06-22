from fastapi import APIRouter
from pydantic import BaseModel

# ✅ This must exist for main.py to work
router = APIRouter(prefix="/habits", tags=["Habits"])

class HabitEntry(BaseModel):
    date: str
    water_intake: float
    sleep_hours: float

habit_db = []

@router.post("/log")
def log_habit(entry: HabitEntry):
    habit_db.append(entry)
    return {"message": "Habit logged!", "data": entry}

@router.get("/all")
def get_all_habits():
    return habit_db
