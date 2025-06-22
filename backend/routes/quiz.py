from fastapi import APIRouter
from fastapi.responses import JSONResponse
import json
import os

router = APIRouter(prefix="/quiz", tags=["Quiz"])

@router.get("/questions")
def get_quiz():
    try:
        file_path = os.path.join(os.path.dirname(__file__), "../data/quiz.json")
        with open(file_path, "r") as f:
            questions = json.load(f)
        return JSONResponse(content=questions)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
