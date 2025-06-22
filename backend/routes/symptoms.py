from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/symptoms", tags=["Symptoms"])

class SymptomEntry(BaseModel):
    date: str
    symptoms: List[str]
    pain_level: int

symptom_db = []

@router.post("/log")
def log_symptom(entry: SymptomEntry):
    symptom_db.append(entry)
    return {"message": "Symptom logged", "data": entry}

@router.get("/all")
def get_all_symptoms():
    return symptom_db
