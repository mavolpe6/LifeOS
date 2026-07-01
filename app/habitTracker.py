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