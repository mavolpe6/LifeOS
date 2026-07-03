class Habit:
    def __init__(self, name:string, description:string, streak:int):
        self.name = name
        self.description = description
        self.streak = streak
    def __str__(self):
        return f"{self.name}: {self.description} - Streak: {self.streak}"
    def __repr__(self):
        return f"Habit(name={self.name}, description={self.description}, streak={self.streak})"
    def __eq__(self, other):
        return self.name == other.name and self.description == other.description and self.streak == other.streak
    def __hash__(self):
        return hash((self.name, self.description, self.streak))
class HabitTracker:
    def __init__(self):
        self.habits = []
    def add_habit(self, habit:Habit):
        self.habits.append(habit)
    def view_habits(self):
        return self.habits
    def remove_habit(self, habit:Habit):
        self.habits.remove(habit)
    def edit_habit(self, habit:Habit, new_name:string, new_description:string):
        habit.name = new_name
        habit.description = new_description


def main():
    add_habit(habit_tracker)
    view_habits(habit_tracker)
habit_tracker = []

def add_habit(added_habit:string):
    habit_tracker.append(added_habit)
    print(f" {added_habit} added to tracker")

def view_habits():
    return habit_tracker
def remove_habit(removed_habit:string):
    if removed_habit in habit_tracker:
        habit_tracker.remove(removed_habit)
        print(f" {removed_habit} removed from tracker")
    else:
        print(f" {removed_habit} not found in tracker")  
def edit_habit(old_habit:string, new_habit:string):
    if old_habit in habit_tracker:
        habit_tracker[habit_tracker.index(old_habit)] = new_habit
        print(f" {old_habit} edited to {new_habit}")
    else:
        print(f" {old_habit} not found in tracker")

if __name__ == "__main__":
    main()