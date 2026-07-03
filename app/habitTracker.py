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
    habit_tracker = HabitTracker()

if __name__ == "__main__":
    main()