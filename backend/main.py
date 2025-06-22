from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import symptoms, habits, quiz

app = FastAPI()

# Allow React frontend to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, set your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include feature routes
app.include_router(symptoms.router)
app.include_router(habits.router)
app.include_router(quiz.router)

@app.get("/")
def root():
    return {"message": "Unified Wellness API is running ✅"}
