from fastapi import FastAPI
from pydantic import BaseModel
from habitTracker import HabitTracker, Habit
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)



class HabitSchema(BaseModel):
    name: str
    description: str
    streak: int
    completed: bool
#get all habits
tracker = HabitTracker()

@app.post("/habits")
def create_habit(new_habit_data: HabitSchema):
    # 1. Build a REAL Habit object using the blueprint from habitTracker.py
    real_habit = Habit(
        name=new_habit_data.name,
        description=new_habit_data.description,
        streak=new_habit_data.streak,
        completed=False  # Required by your __init__!
    )
    
    # 2. Add the real object to your tracker
    tracker.add_habit(real_habit)
    
    # 3. Send a success message back to the frontend
    return {"message": "Success!", "habit_name": real_habit.name}
@app.get("/habits")
def get_all_habits():
    return tracker.view_habits()
@app.delete("/habits/{habit_name}")
def delete_habit(habit_name: str): # Takes a string from the URL
    target_habit = tracker.get_habit(habit_name)
    if target_habit:
        tracker.remove_habit(target_habit)
        return {"message": f"{habit_name} deleted!"}
    return {"error": "Habit not found."}
@app.put("/habits/{habit_name}")
def update_habit(habit_name: str, new_habit: HabitSchema): # Uses Schema, not Habit
    target_habit = tracker.get_habit(habit_name)
    if target_habit:
        tracker.edit_habit(target_habit, new_habit.name, new_habit.description)
        return {"message": f"{habit_name} updated!"}
    return {"error": "Habit not found."}

@app.get("/habits/{habit_name}")
def get_habit_by_name(habit_name: str):
    # Call get_habit ON the tracker instance
    return tracker.get_habit(habit_name)
    