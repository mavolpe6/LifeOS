from fastapi import FastAPI
from pydantic import BaseModel
from habbitTracker import *


app = FastAPI()

class Habit(BaseModel):
    name: str
#create a habit
@app.post("/habits")
 def create_habit(new_habit: Habit):
     new_habit_string= new_habit.name
    add_habit(new_habit_string)
    return {"message": f"Habit {new_habit_string} added"}
#get all habits
@app.get("/habits")
def get_all_habits():
    return{view_habits()}
@app.delete("/habits/{habit_name}")
def delete_habit(habit_name:str):
   return remove_habit(habit_name)
@app.put("/habits/{habit_name}")
def update_habit(habit_name:str, new_habit:Habit):
    return edit_habit(habit_name, new_habit.name)

