from fastapi import FastAPI
from pydantic import BaseModel
from habbitTracker import *
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class Habit(BaseModel):
    name: str
    description: str
    streak: int
#get all habits
@app.post("/habits")
def create_habit(new_habit:Habit):
    return add_habit(new_habit)
@app.get("/habits")
def get_all_habits():
    return view_habits()
@app.delete("/habits/{habit_name}")
def delete_habit(habit_name:str):
   return remove_habit(habit_name)
@app.put("/habits/{habit_name}")
def update_habit(habit_name:str, new_habit:Habit):
    return edit_habit(habit_name, new_habit.name)
@app.get("/habits/habit_name")
def get_habit(habit_name:str):
    return get_habit(habit_name)
    