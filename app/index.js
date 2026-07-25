function SubmitHabit(){
    const habit = document.getElementById("habit").value;
    const frequency = document.getElementById("frequency").value;
    const description = document.getElementById("description").value;
    const completed = document.getElementById("completed").checked;
    console.log(habit, frequency, description, completed);

    const newHabitData={
        name: habit,
        streak: frequency,
        description: description,
    }
    console.log(newHabitData);
}