def main():
    add_habit(habit_tracker)
    view_habits(habit_tracker)
habit_tracker = []

def add_habit(habit_tracker):
    habit = input("Enter a habit: ")
    habit_tracker.append(habit)
    print(f" {habit} added to tracker")

def view_habits(habit_tracker):
    print("Habits:")
    for habit in habit_tracker:
        print(f"- {habit}")
def remove_habit(habit_tracker):
    habit = input("Enter a habit to remove: ")
    if habit in habit_tracker:
        habit_tracker.remove(habit)
        print(f" {habit} removed from tracker")
    else:
        print(f" {habit} not found in tracker")  
def edit_habit(habit_tracker):
    habit = input("Enter a habit to edit: ")
    if habit in habit_tracker:
        new_habit = input("Enter the new habit: ")
        habit_tracker[habit_tracker.index(habit)] = new_habit
        print(f" {habit} edited to {new_habit}")
    else:
        print(f" {habit} not found in tracker")

if __name__ == "__main__":
    main()