from fastapi import FastAPI
from pydantic import BaseModel
from habbitTracker import *


app = FastAPI()

class Habit(BaseModel):
    name: str

@app.post("/habits")
 def create_habit(new_habit: Habit):
     new_habbit_string= new_habit.name
    add_habit(new_habbit_string)
    return {"message": f"Habit {new_habbit_string} added"}


